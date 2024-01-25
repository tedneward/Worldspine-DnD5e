#!/usr/bin/env python3

import argparse
import os
import random
import traceback
import types

error = print

value1 = ("Fred", "Flintstone")

print(type(value1))
print(isinstance(value1, tuple))

def randompick(src):
    if isinstance(src, list):
        return src[random.randint(0, len(src)-1)]
    elif isinstance(src, dict):
        key = list(src.keys())[random.randint(0, len(src)-1)]
        return (key, src[key])
    else:
        error("What the heck is src here?", src)
        return None

l = ['a', 'b', 'c']
m = {'a': 1, 'b': 2, 'c': 3}

print(randompick(l))
print(randompick(m))

def dieroll(dpattern : str) -> int:
    adj = 0
    if dpattern.find("+") > -1:
        adjustmentstr = dpattern.split("+")[1]
        adj = int(adjustmentstr)
        dpattern = dpattern.split("+")[0]
    elif dpattern.find("-") > -1:
        adjustmentstr = dpattern.split("-")[1]
        adj = - int(adjustmentstr)
        dpattern = dpattern.split("-")[0]

    (number, size) = dpattern.split("d")
    if number == '': number = 1
    accum = 0
    for _ in range(int(number)):
        accum += random.randint(1, int(size))
    return accum + adj

print(dieroll("1d4"))
print(dieroll("2d20"))
print("2d20 + 19", dieroll("2d20 + 19"))
print("1d4 - 20", dieroll("1d4 - 20"))
