import math
def f12(x):
    if (x < 181):
        return (x**5)+math.tan(x)
    elif (x >= 181 and x< 254):
        return (x**8)-4*(x**3)+47
    elif (x>=254):
        return 48*(((x**7)+math.cos(x))**3)+math.cos(x)