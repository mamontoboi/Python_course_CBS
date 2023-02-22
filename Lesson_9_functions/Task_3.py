# Нехай на кожну сходинку можна стати з попередньої або переступивши через одну.
# Визначте, скількома способами можна піднятися на задану сходинку.

def step(nums):
    """
    The function that calculates the number of ways to reach "nums" step.
    """
    if nums == 1 or nums == 2:
        return nums
    combs = step(nums - 1) + step(nums - 2)
    return combs


print(f"The quantity of combinations is {step(int(input('Please enter the quantity of steps: ')))}")
