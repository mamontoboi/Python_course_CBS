from random import randint
from Task_3_wheels import *


def inquire():
    qnt = int(input('How many numbers do you want to get? \n'))
    return qnt


def prime_gen():
    yield randint(2, 99)
