def f21(x):
    if x[2] == 1991:
        return 5
    elif x[2] == 2004:
        if x[3] == 'oz':
            return 6
        elif x[3] == 'html':
            return 7
        elif x[3] == 'coq':
            if x[1] == 'nu':
                return 8
            elif x[1] == 'boo':
                return 9
    elif x[2] == 1960:
        if x[3] == 'oz':
            if x[0] == 'hcl':
                return 0
            elif x[0] == 'diff':
                return 1
        elif x[3] == 'html':
            if x[0] == 'hcl':
                return 2
            elif x[0] == 'diff':
                return 3
        elif x[3] == 'coq':
            return 4