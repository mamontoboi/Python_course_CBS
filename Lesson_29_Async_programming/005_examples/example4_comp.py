import asyncio


async def async_worker(number, divider):
    print('Worker {} started'.format(number))
    await asyncio.sleep(0)
    print(number / divider)

# first new loop must be created. Then it must be set.
event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)
# the tasks need to be added to event loop
task_list = [
    event_loop.create_task(async_worker(30, 10)),
    event_loop.create_task(async_worker(20, 10)),
]
# Це завдання чекатиме завершення перших двох.
tasks = asyncio.wait(task_list)
# запускаємо цикл подій до тих пір, поки не виконаються всі завдання.
event_loop.run_until_complete(tasks)
event_loop.close()