
import math
def formu(n,m):
    sum1=0
    sum2=0
    for i in range(n):
        for j in range(m):
            sum1+=((j+1)**4)+math.cos(j+1)+88
    for i in range(n):
        sum2+=math.fabs(i+1)-(i+1)
    c=70*sum1-8*sum2
    return(c)
n=int(input(''))
m=int(input(''))
c=formu(n,m)
print('%.2e'%(c))