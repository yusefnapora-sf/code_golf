import sys

A=list('MDCLXVI')
V=[1000,500,100,50,10,5,1]

with open(sys.argv[1]) as f:
    for l in f:
        n=int(l)
        s=''
        t=[0] * 7
        i=0
        while n > 0:
            t[i], n = divmod(n, V[i])
            i+=1

        for i in range(7):
            if t[i] < 4:
                s += A[i] * t[i]
            else:
                y = t[i-1]
                s = s[:len(s)-y] + A[i] + A[i-1-y]
        print(s)
