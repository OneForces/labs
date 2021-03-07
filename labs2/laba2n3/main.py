def f23(table):
    for r in table:
        if r[0] is None:
            del r[0]

    for r in table:
        tmp = r[0].split(';')
        r[0] = str(round(float(tmp[1]) ,1))
        if r[1] == "Не выполнено":
            r[1] = "нет"
        else:
            r[1] = "да"
        r.append(tmp[0].split('@')[1])
    return [list(r) for r in zip(*table)]