import time
import asyncio
import random
import threading
import requests
import aiohttp



# async def hello(name):
#     delay = random.randint(1,3)
#     await asyncio.sleep(delay)
#     print(f'Hello {name}')
# names = ["Оля", "Іван", "Марія"]
# async def main():
#     await asyncio.gather(*(hello(name)for name in names))
# if __name__ =='__main__':
#     asyncio.run(main())

#>>>>>>>>>>>>>>>SYNCED<<<<<<<<<<<<<<<<<<<<<
# def task(name):
#     print(f'name {name} start')
#     time.sleep(2)
#     print(f"{name} done")
#
# def main():
#     for t in['A','B','C']:
#         task(t)
# if __name__ == '__main__':
#     main()

#>>>>>>>>>>>>>>>>>ASYNCED<<<<<<<<<<<<<<<<
# async def task(name):
#     print(f'name {name} start')
#     await asyncio.sleep(2)
#     print(f"{name} done")
#
# async def main():
#     await asyncio.gather(task('A'), task('B'), task('C'))
#
# if __name__ == '__main__':
#     asyncio.run(main())

#>>>>>>>>>>>>THREADS<<<<<<<<<<<<<<<

# def sync_task(name):
#     print(f'name {name} start')
#     time.sleep(2)
#     print(f"{name} done")
#
# threads = []
# for t in ['A','B','C']:
#     th = threading.Thread(target=sync_task,args=(t,))
#     threads.append(th)
#     th.start()
# for th in threads:
#     th.join()



#>>>>>>>>>>>>>>>>HTTP requests SYNCED<<<<<<<<<<<<<<<<<<<<
# urls = ['https://itstep.org']*5
# start = time.time()
# for url in urls:
#     r = requests.get(url)
#     print(f"got {len(r.text)} symbols")
#
# print(f"time: {time.time()-start}")

#>>>>>>>>>>>>>>>>HTTP requests ASYNCED<<<<<<<<<<<<<<<<<<<<

# async def fetch(session,url):
#     async with session.get(url) as response:
#         text = await response.text()
#         print(f"got {len(text)} symbols")
#         return text
#
# async def main():
#     urls = ['https://itstep.org']*1000
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch(session,url) for url in urls]
#         await asyncio.gather(*tasks)
# start = time.time()
# asyncio.run(main())
# print(f"time: {time.time()-start}")


# async def producer(queue):
#     for i in range(5):
#         await asyncio.sleep(random.uniform(0.5,1.5))
#         item = f"task-{i}"
#         await queue.put(item)
#         print(f'Producer add {item}')
#
# async def consumer(queue):
#     while True:
#         item = await queue.get()
#         print(f"Consumer do {item}")
#         await asyncio.sleep(random.uniform(1,2))
#         queue.task_done()
#
# async def main():
#     queue = asyncio.Queue()
#     await asyncio.gather(
#         producer(queue),
#         consumer(queue),
#     )
# asyncio.run(main())

async def countdown(name: str, total_seconds: int):
    for remaining in range(total_seconds, 0, -1):
        print(f"[{name}] started for {total_seconds}s → {remaining}s left")
        await asyncio.sleep(1)
    print(f"[{name}] DONE! ({total_seconds}s timer)")

async def main():
    await asyncio.gather(
        countdown("Timer A", 5),
        countdown("Timer B", 8),
        countdown("Timer C", 3),
    )

if __name__ == "__main__":
    asyncio.run(main())


