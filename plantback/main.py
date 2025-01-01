import asyncio
import multiprocessing
import time
from MMQT.mqttclient import mqtt_client_process

from  webstocket import websocket_process

def start_processes():
    message_queue = multiprocessing.Queue()


    # 启动 MQTT 客户端进程
    mqtt_process = multiprocessing.Process(target=mqtt_client_process,args=(message_queue,))
    mqtt_process.start()
    print(f"MQTT 客户端进程启动，PID: {mqtt_process.pid}")


    # 启动 WebSocket 服务器进程
    websocket_proc = multiprocessing.Process(target=websocket_process, args=(message_queue,))
    websocket_proc.start()
    print(f"WebSocket 服务器进程启动，PID: {websocket_proc.pid}")


    try:
        while True:
            time.sleep(1)  # 主进程保持运行
    except KeyboardInterrupt:
        print("主进程收到终止信号，正在停止子进程...")
        if mqtt_process.is_alive():
            mqtt_process.terminate()  # 终止 MQTT 客户端进程
            mqtt_process.join()
            print("MQTT 客户端进程已终止")

        if websocket_proc.is_alive():
            websocket_proc.terminate()
            websocket_proc.join()
            print("WebSocket 服务器进程终止")

    print("主进程结束")

if __name__ == "__main__":
    start_processes()
