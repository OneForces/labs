import math

def form(x):
    if (x < 181):
        c = (x**5)+math.tag(x)
    elif (x >= 181 and x< 254):
        c = (x**8)-4*(x**3)+47
    elif (x>=254):
        c = 48*(((x**7)+math.cos(x))**3)+math.cos(x)
    return c


x=int(input('x = '))
c = form(x)
print('%.2e'%c)