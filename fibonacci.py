from functools import lru_cache
import sys

sys.setrecursionlimit(12023)


@lru_cache(maxsize=None)
def f(n):
    if n < 3:
        return 1
    else:
        return f(n-1) + f(n-2)
        
print(f(3))    