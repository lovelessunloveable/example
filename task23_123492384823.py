

def f23(x,y,z):
    if x>y+100:
        return 0
    if x==y:
        return 1
    if z=="a":
        return f23(x*2,y,"b")+f23(x*3,y,"c")
    if z!="a":
        return f23(x-1,y,"a") +f23(x*2,y,"b")+f23(x*3,y,"c")
print(f23(3,15,""))