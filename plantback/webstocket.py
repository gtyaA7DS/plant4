import asyncio
import websockets
import os

def websocket_process(queue, host="0.0.0.0", port=8764):
    connected_clients = set()
    lock = asyncio.Lock()

    async def handler(websocket):
        # 添加新连接的客户端
        async with lock:
          connected_clients.add(websocket)
        print("客户端已连接")
        try:
            while True:
                if not queue.empty():  # 如果队列中有消息
                    message = queue.get()  # 获取消息
                    async with lock:
                        clients = list(connected_clients)  # 创建副本
                    # 向所有连接的客户端广播消息
                    for client in clients:
                        try:
                            await client.send(message)
                            print(f"主动推送消息:{message}")
                        except websockets.ConnectionClosed:
                            print("发送失败，客户端已断开")
                            async with lock:
                             connected_clients.remove(client)

                await asyncio.sleep(2)  # 等待新消息
        except websockets.ConnectionClosed:
            print("客户端断开连接")
        finally:
            # 移除断开的客户端
            async with lock:
               connected_clients.remove(websocket)

    # WebSocket 服务器启动
    async def start_server():
        server = await websockets.serve(handler, host, port)
        print("WebSocket 服务器启动，等待客户端连接...")
        await server.wait_closed()

    asyncio.run(start_server())
