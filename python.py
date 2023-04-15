import sys
import math
from contextlib import redirect_stdout

def compute_multiples_sum(n):
    sum = 0
    for i in range(1,n):
        if  i % 5 == 0 or i % 3 ==0 or i % 7 == 0:
            print(i)
            sum = sum + i
    print(sum)


compute_multiples_sum(10)
