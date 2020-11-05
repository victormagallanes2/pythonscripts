import asyncio

# definimos la función
async def show_seconds():
    while True:
        for i in range(60):
            print(i, 's')
            await asyncio.sleep(1)


async def show_minute():
    for i in range(1, 10):
        await asyncio.sleep(60)
        print(i, 'minuto')


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(show_seconds(), show_minute()))
loop.close()
# Con gather, podemos ejecutar las dos rutinas 
# simultaneamente