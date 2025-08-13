import sys

A=list('MDCLXVI')
D=(2,5)

for l in open(sys.argv[1]):
    n=int(l)
    s=''
    t=[0] * 7
    i=0
    v=1000
    while n > 0:
        t[i], n = divmod(n, v)

        if t[i] < 4:
            s += A[i] * t[i]
        else:
            y = t[i-1]
            s = s[:len(s)-y] + A[i] + A[i-1-y]

        v //= D[i%2]
        i+=1
    print(s)
