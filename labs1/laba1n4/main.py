def f14(n):
   if (n==0):
       return 3
   else:
       c = ((1/74)*(f14((n-1))**2))-(1/6)*(f14(n-1))
       return c
