import time
import paho.mqtt.client as mqtt
import random
import json

# MQTT 配置
MQTT_BROKER = "124.222.214.78"  # 替换为你自己的 MQTT 服务器 IP
MQTT_PORT = 1883
MQTT_TOPIC = "home/sensors/data"  # 你想要发布数据的主题

# MQTT 事件回调函数
def on_connect(client, userdata, flags, rc):
    """连接成功时调用"""
    if rc == 0:
        print("连接成功")
    else:
        print(f"连接失败，错误码：{rc}")

def on_publish(client, userdata, mid):
    """消息发布成功时调用"""
    print(f"消息发布成功，消息 ID：{mid}")

# 创建 MQTT 客户端
client = mqtt.Client("PythonClient")

# 设置回调函数
client.on_connect = on_connect
client.on_publish = on_publish

# 连接到 MQTT 服务器
def connect_mqtt():
    try:
        print("连接到 MQTT 服务器...")
        client.connect(MQTT_BROKER, MQTT_PORT)
        print("MQTT 连接成功！")
    except Exception as e:
        print(f"MQTT 连接失败，错误: {e}")
        time.sleep(5)

# 生成模拟的空气质量数据 (随机整数)
def get_air_quality_data():
    pm1 = random.randint(10, 45)  # 模拟 PM1 数据，随机整数
    pm25 = random.randint(10, 65)  # 模拟 PM2.5 数据，随机整数
    pm10 = random.randint(15, 75)  # 模拟 PM10 数据，随机整数
    return pm1, pm25, pm10

# 生成模拟的湿度和温度数据 (保留两位小数)
def get_dht11_data():
    humidity = round(random.uniform(50, 80), 2)  # 随机湿度值，保留两位小数
    temperature = round(random.uniform(15, 20), 2)  # 随机温度值，保留两位小数
    return humidity, temperature

# 发布传感器数据到 MQTT
def publish_sensor_data():
    # 获取空气质量数据（模拟 PMS5003）
    pm1, pm25, pm10 = get_air_quality_data()

    # 获取湿度和温度数据（模拟 DHT11）
    humidity, temperature = get_dht11_data()

    # 创建 JSON 数据
    sensor_data = {
        "pm1": pm1,
        "pm25": pm25,
        "pm10": pm10,
        "temperature": temperature,
        "humidity": humidity
    }

    # 将数据转换为 JSON 字符串
    json_data = json.dumps(sensor_data)

    # 发布数据到 MQTT
    client.publish(MQTT_TOPIC, json_data)
    print(f"传感器数据已发送: {json_data}")

# 主函数
def main():
    connect_mqtt()
    client.loop_start()  # 启动 MQTT 客户端循环

    while True:
        publish_sensor_data()  # 发布数据
        time.sleep(15)  # 每5秒发布一次数据
        # 定期调用 loop() 方法，以确保 MQTT 客户端连接保持活跃并处理网络事件
        client.loop()  # 处理网络事件

if __name__ == "__main__":
    main()
