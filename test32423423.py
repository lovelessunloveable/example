import sys
sys.setrecursionlimit(99999)
def f23(x,y):

    if x>y or x==17:
        return 0
    elif x==y:
        return 1
    return f23(x+2,y) +f23(x+3,y)+f23(x*2,y)
print(f23(3,10)*f23(10,25))


def osnvolna20(x,y):

    if x<y or x==9 or x==16:
        return 0
    elif x==y:
        return 1
    return osnvolna20(x-1,y) +osnvolna20(x-2,y)+osnvolna20(x//3,y)
print(osnvolna20(19,3))


def osnvolna27(x,y):

    if x<y or x==7:
        return 0
    elif x==y:
        return 1
    return osnvolna27(x-1,y) +osnvolna27(x-3,y)+osnvolna27(x//2,y)
print(osnvolna27(19,10)*osnvolna27(10,3))
