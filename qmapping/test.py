import string
from os import listdir

import cvxpy as cp
import math
import numpy as np


def mod(v: list):
    for i in v:
        if isinstance(i, int) and i == 0:
            return 0
        if not isinstance(i, int) and i.value == 0:
            return 0
        if not isinstance(i, int) and i.value == 1:
            pass
    return 1


print(mod([5, 3]))

v = cp.Variable(boolean=True, integer=True)
v1 = cp.Variable(boolean=True, integer=True)
v2 = cp.Variable(boolean=True, integer=True)
para = cp.Parameter(integer=True)
para.value = 1
c_1 = cp.Parameter(integer=True)
c_1.value = 1
num = cp.Parameter(integer=True)
num.value = 2
num1 = cp.Parameter(integer=True)
num1.value = 3
pa = cp.Variable(boolean=True)
prob = cp.Problem(cp.Minimize((c_1 * mod(cp.vstack([1, v, v2]))) + (num * v2) + (num1 * v1)),
                  [
                      v + v1 + v2 == c_1])
print(prob)

print("isdcp: ", prob.objective.is_dcp())
prob.solve(verbose=True)  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var:")
print(v.value, v1.value, v2.value)
