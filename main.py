import random

def create(b,low,high,n):
    for i in range(n):
        b.append(random.randint(low, high))

def find0(b):
    for m in range(len(b)):
        if b[m]==0:
            return mult(b,m+1,1)
            break
        if m==len(b)-1:
            return 'Немає нулів'

def max(imax,nmax,a,i):
    while i<len(a):
        if a[i] > nmax:
            nmax = a[i]
            imax = i
        i+=1
    return imax


def mult(b,m,v):
    while m <len(b):
        v*=b[m]
        if b[m]==b[-1]:
            return '1 Нуль'
        if b[m+1]!=0:
            m+=1
            continue
        else:
            return v

def shift(b,i,k):
    if len(b)%2==1:
        t=0
    else:
        t=-1
    while i<=len(b)//2+t and k<=len(b)//2+t:
        b[i], b[i+k] = b[i+k], b[i]
        k+=1
        i+=1

def main():
    b=[]
    n=(int(input('n=')))
    low = (int(input('low=')))
    high = (int(input('high=')))
    create(b,low,high,n)
    print(b)
    print('N='+str(max(0, b[0], b, 0)+1))
    print(find0(b))
    shift(b,1,1)
    print(b)

if __name__=='__main__':
    main()
