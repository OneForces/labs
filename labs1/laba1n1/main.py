import math
def formu(x, y):
    c = ((94*(x**6)+math.cos(x)-37)/(96*(x**2)-(y**6)+98))-(((x**6)/50)-(y**2)+94)+((66*y+(y**5))/(70*(x**7)-45*(x**4)))
    return (c)

x = int(input('1nd = '))
y = int(input('2nd = '))
c = formu(x, y)
print(f'F({x},{y})=', '%.2e' % (c))