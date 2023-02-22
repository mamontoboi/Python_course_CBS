import asyncio


# defines coroutines
async def main():
    print('Hello!')
    await foo('Foo!')  # await fo func foo to finish
    print('Finish!')  # continue after foo is completed.


async def foo(text):
    print(text)
    await asyncio.sleep(1)  # commands to stop and sleep for 1 sec

# event loop required to start coroutine
asyncio.run(main())


""" 1) Prints in the following order:
main print 'Hello!' --> main awaits for foo to start and finish --> foo prints 'Foo' -->
--> foo completed --> main resumes --> main prints 'Finish!'
I.e. the code in main was stopped and waiting for foo to finish."""


"""2) asyncio.create_task means that the command to execute func foo was given, 
but it must be executed only when there are no any other funcs in operation. 
No need to stop the process for execution of task"""
async def main():
    print('Main!')
    task = asyncio.create_task(fuz('Fuz!'))  # initiates task fuz, but not execute it
    print('Finish!')  # competes main, execute fuz


async def fuz(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())

""" Prints in the following order: 
    Main!
    Finish!
    Fuz!
    Executes main func first, then task."""

"""3) await task means that main will wait for buz to finish. Same as in paragraph 1"""
async def main():
    print('Main!')
    task = asyncio.create_task(buz('Buz!'))
    await task  # awaits for task to complete before continue main
    print('Finish!')


async def buz(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())

""" Prints in the following order: 
    Main!
    Buz!
    Finish!
    Starts main, then waits for task (buz) to complete, then finishes the main."""


"""4) await task means that main will wait for buz to finish. Same as in paragraph 1"""
async def main():
    print('Main!')
    task = asyncio.create_task(buz('Buz!'))
    await asyncio.sleep(2)  # main falls asleep for 2 seconds
    print('Finish!')


async def buz(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())

""" Prints in the following order: 
    Main!
    Buz!
    Finish!
    Starts main, then initiates task, but not executes. Then main falls asleep. Task (buz) is executed (due to main on halt). 
    Then the main awakes and is finished."""

