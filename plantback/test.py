import asyncio

async def worker(lock, name):
    print(f"{name} is waiting for the lock")
    async with lock:
        print(f"{name} has acquired the lock")
        await asyncio.sleep(1)  # 模拟一些异步操作
    print(f"{name} has released the lock")

async def main():
    lock = asyncio.Lock()
    await asyncio.gather(
        worker(lock, "Worker 1"),
        worker(lock, "Worker 2"),
        worker(lock, "Worker 3")
    )

asyncio.run(main())
