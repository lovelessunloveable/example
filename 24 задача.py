import re

def osnovnayaVolna():
    pat=re.compile(r'[1-9A-F][0-9A-F]*')
    m=pat.findall(open('24_9791.txt').readline())
    print(m[:5])
    print(len(max(m,key=len)))

def osnovnayaVolna2():
    pat=re.compile(r'((8|9)?([A-C][8-9])+(A|B|C)?)')
    m=pat.findall(open('24_9845.txt').readline())
    print(m[:5])
    m=[x[0]for x in m]
    print(len(max(m,key=len)))

def egkr16():
    pat=re.compile(r'(SQ|Q)?(RSQ)+(RS|R)?')
    m=pat.findall(open('24_12254.txt').readline())
    print(m[:5])
    print(len(max(m,key=len)))

def polyak():
    pat=re.compile(r'(?<=KK)(43..78...34)(?=KK)')
    m=pat.findall(open('polyakov.txt').readline())
    m=[int(x) for x in m]
    maxi=max(m)
    p=1
    for x in str(maxi):
        if int(x)%2!=0:
            p=p*int(x)

    print(p)

def demo2024():
    pat=re.compile(r'(?=(([^T]*[T]){101}))')
    m=pat.findall(open('24_10105.txt').readline())
    m=[x[0]for x in m]
    print(len(max(m,key=len)))

print(demo2024())