#include <WiFi.h>
#include <PubSubClient.h>
#include <Adafruit_PM25AQI.h>
#include <DHT.h>
#include <HardwareSerial.h>
#include <ArduinoJson.h>  // 引入 ArduinoJson 库

// PMS5003 串口通信配置
HardwareSerial mySerial(1);  // 使用 UART1
Adafruit_PM25AQI aqiSensor;

// DHT11 配置
#define DHTPIN 4       // DHT11 数据引脚连接到 GPIO4
#define DHTTYPE DHT11   // 使用 DHT11 类型传感器
DHT dht(DHTPIN, DHTTYPE);

// Wi-Fi 配置
const char* ssid = "yae";         // Wi-Fi 名称
const char* password = "pkcccccc"; // Wi-Fi 密码

// MQTT 配置
const char* mqtt_server = "124.222.214.78";  // MQTT 服务器 IP
const int mqtt_port = 1883;                 // MQTT 服务器端口

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  // 初始化串口用于调试
  Serial.begin(115200);

  // 初始化 Wi-Fi
  setupWiFi();

  // 初始化 MQTT
  client.setServer(mqtt_server, mqtt_port);

  // 初始化 PMS5003
  mySerial.begin(9600, SERIAL_8N1, 16, 17);  // PMS5003 串口初始化，RX=16, TX=17
  if (!aqiSensor.begin_UART(&mySerial)) {
    Serial.println("无法初始化 PMS5003 传感器。请检查连接！");
    while (1) delay(10);
  }
  Serial.println("PMS5003 初始化成功！");

  // 初始化 DHT11
  dht.begin();
}

void loop() {
  // 检查 MQTT 是否连接，如果没有连接则重新连接
  if (!client.connected()) {
    reconnectMQTT();
  }
  client.loop();

  // 读取 PMS5003 数据
  PM25_AQI_Data data;
  if (aqiSensor.read(&data)) {
    String pm1 = String(data.pm10_env);
    String pm25 = String(data.pm25_env);
    String pm10 = String(data.pm100_env);

    // 读取 DHT11 数据
    float h = dht.readHumidity();    // 获取湿度
    float t = dht.readTemperature(); // 获取温度

    // 检查 DHT11 是否读取成功
    if (isnan(h) || isnan(t)) {
      Serial.println("读取 DHT11 数据失败！");
    } else {
      // 构建 JSON 对象
      StaticJsonDocument<512> doc;
      doc["pm1"] = pm1;
      doc["pm25"] = pm25;
      doc["pm10"] = pm10;
      doc["temperature"] = String(t);
      doc["humidity"] = String(h);

      // 将 JSON 数据序列化为字符串
      char jsonBuffer[512];
      serializeJson(doc, jsonBuffer);

      // 发送 JSON 数据到 MQTT
      client.publish("home/sensors/data", jsonBuffer);

      // 输出到串口调试
      Serial.println("传感器数据发送成功！");
      Serial.println(jsonBuffer);
    }
  } else {
    Serial.println("读取 PMS5003 数据失败！");
  }

  delay(5000);  // 每两秒读取一次并发送数据
}

// 连接 Wi-Fi
void setupWiFi() {
  delay(10);
  Serial.println();
  Serial.print("连接到 Wi-Fi ");
  Serial.print(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("Wi-Fi 连接成功！");
  Serial.print("IP 地址: ");
  Serial.println(WiFi.localIP());
}

// 重新连接 MQTT
void reconnectMQTT() {
  while (!client.connected()) {
    Serial.print("尝试连接 MQTT...");

    if (client.connect("ESP32Client")) {  // 去掉用户名和密码
      Serial.println("连接成功！");
    } else {
      Serial.print("连接失败，状态码：");
      Serial.print(client.state());
      delay(5000);
    }
  }
}
