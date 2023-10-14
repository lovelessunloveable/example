from turtle import *
import sys
sys.setrecursionlimit(99999)
from itertools import product
def f2():
    print('x y z w')
    for x in range(2):
       for y in range(2):
          for z in range(2):
             for w in range(2):
                if (not(y<=x) or (z<=w) or not(z))==False:
                   print(x, y, z, w)

def f5():
    for i in range(1,100):
        num=(bin(i)[2:])
        if num.count('1')%2==0:
            chislo='10'+num[2:]+'0'

        if num.count('1')%2!=0:
            chislo='11'+num[2:]+'1'
        if int(chislo,2)>40:
            print (i, int(chislo,2))
            break

def f6():
    left(90)
    for i in range(7):
        forward(300)
        right(120)
    pu()
    for x in range(1,9):
        for y in range(1,10):
            goto(x*30,y*30)
            dot(2)
    done()

def f8():
    k=0
    n='16 36 56 76 61 63 65 67'
    nn=n.split()
    nums=product('01234567',repeat=5)
    for n in nums:
        numb=''.join(n)
        if numb.count('6')==1 and numb[0]!='0':
            if all(not(x in numb) for x in nn):
                k+=1
    print(k)

def f12():
        for n in range (4, 10000):
            s = '5' + n*'2'
            while '52' in s or '2222' in s or '1122' in s:
                s = s.replace ('52', '11', 1)
                s = s.replace ('2222', '5', 1)
                s = s.replace ('1122', '25', 1)
                if sum(map(int,s)) == 64:
                    print (n)

def f16a():
        #sys.setrecursionlimit(2500)
    itog1=itog2=1
    for x1 in range(1,2024):
        itog1=itog1*x1
    for x2 in range(1,2021):
        itog2=itog2*x2
    print(itog1/itog2)

def F(n):
    if n == 1: return n
    if n>1: return n*F(n-1)
print(F(2023)/F(2020))

def f17():
    with open('17_4705.txt') as f:  
        nums=[int(x) for x in f]
        maxi=[]
        s=[]
       
        for i in range(len(nums)):
          if nums[i]%10==3:
             maxi.append(nums[i])
        maximum=0
        for i in range(len(nums)-1):
            a=abs(nums[i])%10
            b=abs(nums[i+1])%10
            if ((a==3) and (b!=3)) or ((a!=3) and (b==3)):
                if (nums[i]**2+nums[i+1]**2) >= max(maxi)**2: 
                    s.append(nums[i]+nums[i+1])
                if nums[i]**2+nums[i+1]**2>maximum:
                    maximum=nums[i]**2+nums[i+1]**2
    print(len(s), maximum)

def f(a,m):
        if a>77: return m%2==0
        if m==0: return 0
        actions=(a+1),(a+4),(a*4)
        steps=[f(a,m-1) for a in actions]
        if m%2==0: return all(steps)
        else: return any(steps)
s20=[s for s in range(1,78) if not f(s,1) and f(s,3)]
print(s20)
s21=[s for s in range(1,78) if f(s,4)]
print(min(s21))

def f23(x,y):
    if x>y or x==17:
        return 0
    elif x==y:
        return 1
    return f23(x+1,y) +f23(x*2,y)
print(f23(1,10)*f23(10,35))

def f24():
    with open('24_4710.txt') as f:
        s=f.readline().replace('C','S').replace('D','S').replace('F','S')
        s=s.replace('A','G').replace('O','G')
        s=s.replace('SG','*')
        k=kmax=0
        for i in s:
            if i=='*':
                k+=1
                kmax=max(k,kmax)
            else:k=0
    print(kmax)

def f25():
    for i in range(2023,10**10,2023):
        num=str(i)
        if num[0]=='1' and num[2:6]=='2139' and num[-1]=='4':
            print(i,i//2023)

def f26():
    with open('26_4712.txt') as f:
        s=[int(x) for x in f]
        s=sorted(s[1:],reverse=True)
        k,mini=1,s[0]

    for i in range(1,len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
    print(k,mini)

f26()
