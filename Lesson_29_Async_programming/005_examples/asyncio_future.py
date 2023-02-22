import asyncio
"""
Future is a variable, that will receive value in a future, during execution of the program.
"""

"""Example 1, with tasks and future"""

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)  # program starts then falls asleep
    print('done fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    # create task to add task to event loop
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1  # value is FUTURE. It expects task1 to finish to assign the data to value
    print(value)
    await task2  # waits for task 2 to finish before end of program

asyncio.run(main())

"""
start fetching
0
1
2
3
4
5
6
7
done fetching
{'data': 1}  -- end of task1, fetch_data func
8
9  -- end of task2
"""

"""Example 2, without tasks and without future"""

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)  # program starts then falls asleep
    print('done fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    await fetch_data()  # coroutine waits for fetch_data to finish
    task2 = asyncio.create_task(print_numbers())

    await task2  # waits for task 2 to finish before end of program

asyncio.run(main())

"""
start fetching
done fetching -- end of fetch_data func
0
1
2
3
4
5
6
7
8
9 -- end of print numbers

"""