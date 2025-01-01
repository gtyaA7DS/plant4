import json

import paho.mqtt.client as mqtt
from sql.handlesql import db



def mqtt_client_process(queue,mqtt_server="127.0.0.1", mqtt_port=1883, topic="home/sensors/#"):
    def check_air_quality(data):
        # 定义正常范围
        normal_ranges = {
            'pm10': (0, 50),  # PM10 的正常范围
            'pm25': (0, 35),  # PM2.5 的正常范围
            'pm1': (0, 25),  # PM1 的正常范围
            'temperature': (0, 35),  # 温度的正常范围，假设 0 到 35 摄氏度
            'humidity': (30, 60)  # 湿度的正常范围，假设 30% 到 60%
        }

        # 存放报警信息的列表
        alarms = []

        # 检查各个参数的值
        for key, value in data.items():
            if key not in normal_ranges:
                continue  # 跳过不需要检查的键

            min_value, max_value = normal_ranges[key]

            if not min_value <= value <= max_value:
                # 针对不同的参数生成具体的报警信息
                if key == 'pm10' or key == 'pm25' or key == 'pm1':
                    if value > max_value:
                        alarms.append(f"报警：{key} 值 {value} 超出阈值 {max_value}，空气质量浑浊")
                elif key == 'humidity':
                    if value < min_value:
                        alarms.append(f"报警：湿度值 {value} 过低，请启动加湿器")
                    elif value > max_value:
                        alarms.append(f"报警：湿度值 {value} 过高，空气潮湿")
                elif key == 'temperature':
                    if value > max_value:
                        alarms.append(f"报警：温度值 {value} 过高，环境过热")
                    elif value < min_value:
                        alarms.append(f"报警：温度值 {value} 过低，环境过冷")

        # 如果有报警信息，返回报警信息，否则返回“所有值正常”
        if alarms:
            return '\n'.join(alarms)
        else:
            return "所有值正常"


    # 当连接到 MQTT 服务器时调用的回调函数
    def on_connect(client, userdata, flags, rc):
        print(f"连接成功，状态码 {rc}")
        print("订阅主题:", topic)
        # 连接成功后订阅主题
        client.subscribe(topic)

    # 当收到消息时调用的回调函数
    def on_message(client, userdata, msg):
        print(f"收到消息: {msg.topic} -> {msg.payload.decode()}")
        data_dict = json.loads(msg.payload.decode())
        data_dict = {key: float(value) for key, value in data_dict.items()}

        db.insertairqualitydate(data_dict)
        res=check_air_quality(data_dict)
        if res != "所有值正常":

            queue.put(res)


    # 创建 MQTT 客户端
    client = mqtt.Client()

    # 设置回调函数
    client.on_connect = on_connect
    client.on_message = on_message

    # 连接到 MQTT 服务器
    client.connect(mqtt_server, mqtt_port, 60)

    # 保持客户端运行并等待消息
    client.loop_forever()
