def task_1(dane: list[str]) -> int:
    result = 0
    parsed = []
    dane = [z.split(' ') for z in dane]
    while True:
        length = 0
        for i in dane:
            length += len(i) 
        for i in dane:
            for idx, j in enumerate(i):
                if j == '':
                    i.pop(idx)
        length2 = 0
        for i in dane:
            length2 += len(i)
        if length == length2:
            break

    for i in dane[:-1]:
        i = list(map(int, i))
        parsed.append(i)
    
    parsed.append(dane[-1])

    for i in range(len(parsed[0])):
        znak = parsed[-1][i]
        if znak == '+':
            wynik = 0
        else:
            wynik = 1
        for j in range(len(parsed) - 1):
            if znak == '+':
                wynik += parsed[j][i]
            if znak == '*':
                wynik *= parsed[j][i]
        result += wynik
    return result

def task_2(dane: list[str]) -> int:
    parsed = []
    parsed2 = []
    parsed3 = []
    parsed4 = []
    result = 0
    
    for i in dane:
        temp = []
        for j in i:
            temp.append(j)
        parsed.append(temp)
   
    for i in range(len(parsed[0])):
        temp = ''
        for j in range(len(parsed)):
            try:
                temp += parsed[j][i]
            except Exception:
                continue
        parsed2.append(temp)
     
    idx = 0
    temp = []
    parsed2.append('koniec')
    while True:
        if len(set(parsed2[idx])) == 1:
            parsed3.append(temp)
            temp = []
        elif parsed2[idx] == 'koniec':
            parsed3.append(temp)
            break
        else:
            temp.append(parsed2[idx])
        idx += 1
    
    znaki = []
    for i in range(len(parsed3)):
        for j in range(len(parsed3[i])):
            if parsed3[i][j][-1] in '*+':
                znaki.append(parsed3[i][j][-1])
                parsed3[i][j] = parsed3[i][j][:-1]
    for i in range(len(parsed3)):
        parsed4.append(list(map(int, parsed3[i])))
    
    idx = 0
    for i in parsed4:
        znak = znaki[idx]
        if znak == '+':
            wynik = 0
        else:
            wynik = 1
        for j in i:
            if znak == '+':
                wynik += j
            if znak == '*':
                wynik *= j
        idx += 1     
        result += wynik
    return result
