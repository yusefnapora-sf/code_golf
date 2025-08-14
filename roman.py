import sys

A=list('MDCLXVI')
D=(2,5)

for l in open(sys.argv[1]):
    n=int(l)
    s=''
    t=[]
    i=0
    v=1000
    while n > 0:
        f, n = (n//v, n%v)

        if f < 4:
            s += A[i] * f
        else:
            y = t[i-1]
            s = s[:len(s)-y] + A[i] + A[i-1-y]

        v //= D[i%2]
        t += [f]
        i+=1
    print(s)
