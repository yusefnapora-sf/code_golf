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
        t[i], n = (n//v, n%v)

        s += A[i] * t[i]
        q = t[i] // 4
        x = t[i-1]
        s = s[:len(s)-(3-x)*q] + A[i-1-x]*q

        v //= D[i%2]
        i+=1
    print(s)
