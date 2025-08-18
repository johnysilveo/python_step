import asyncio
import aiofiles


async def countdown(name:str,total_seconds:int):
    for i in range(total_seconds):
        print(f"{name} set for {total_seconds} seconds.")
        await asyncio.sleep(1)
    print(f"[{name}] DONE!")
async def main():
    await asyncio.gather(
        countdown("timer 1", 0),
        countdown("timer 2", 0),
        countdown("timer 3", 0),)
if __name__ == "__main__":
    asyncio.run(main())

#>>>>>>>>>>>>>>>>>DOWNLOAD<<<<<<<<<<<<<<<

async def download_file_1():
    await asyncio.sleep(3)
    print('File 1 downloaded')
async def download_file_2():
    await asyncio.sleep(2)
    print('File 2 downloaded')
async def download_file_3():
    await asyncio.sleep(1)
    print('File 3 downloaded')
async def main():
    await asyncio.gather(download_file_1(),
                         download_file_2(),
                         download_file_3()
                         )
if __name__ == '__main__':
    asyncio.run(main())

#>>>>>>>>>>>>>>>>>>>>>>FILESSSSSSSSSSSS<<<<<<<<<<<<<<<<<<<

async def async_write_file(name: str, text: str):
    async with aiofiles.open(f"{name}.txt", "w", encoding="utf-8") as file:
        await file.write(text)

async def async_read_file(name: str):
    async with aiofiles.open(f"{name}.txt", "r", encoding="utf-8") as file:
        text = await file.read()
        print(f"This is file {name}: {text}")
    return text

async def main():
    await asyncio.gather(
        async_write_file("File1", "This is file 1"),
        async_write_file("File2", "This is file 2"),
        async_write_file("File3", "This is file 3"),
    )
    await asyncio.gather(
        async_read_file("File1"),
        async_read_file("File2"),
        async_read_file("File3"),
    )
if __name__ == "__main__":
    asyncio.run(main())


