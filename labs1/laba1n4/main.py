def formu(n):
   if (n==0):
       return 3
   else:
       c = ((1/74)*(formu((n-1))**2))-(1/6)*(formu(n-1))
       return c
n=int(input(''))
c=formu(n)
print('%.2e'%(c))
