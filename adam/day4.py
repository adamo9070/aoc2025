def read_data(file: str) -> list[list[str]]:
    dane = []
    with (open(file, 'r') as F):
        temp =  [z.strip() for z in F]
        for i in temp:
            temp2 = []
            for j in i:
                    temp2.append(j)
            dane.append(temp2)
    return dane

def task_1(dane: list[list[str]]) -> int:
    result = 0
    # robie buffer zone na okolo danych
    dane.insert(0, ['x'] * len(dane[0]))
    dane.append(['x'] * len(dane[0]))
    for i in range(len(dane)):
        dane[i].insert(0, 'x')
        dane[i].append('x')

    #jak kod dziala to jest dobry pozdro    
    for i in range(len(dane)):
        for j in range(len(dane[0])):
            sasiedzi = ''
            if dane[i][j] == '@':
                try:
                    if dane[i+1][j-1] == '@':
                        sasiedzi += '@'
                except IndexError:
                    sasiedzi += ''
                try:
                    if dane[i+1][j] == '@':
                        sasiedzi += '@'
                except IndexError:
                    sasiedzi += ''
                try:
                    if dane[i+1][j+1] == '@':
                        sasiedzi += '@'
                except IndexError:
                    sasiedzi += ''
                try:
                    if dane[i][j-1] == '@':
                        sasiedzi += '@'
                except IndexError:
                    sasiedzi += ''
                try:
                    if dane[i][j+1] == '@':
                        sasiedzi += '@'
                except IndexError:
                    sasiedzi += ''
                try:
                    if dane[i-1][j-1] == '@':
                        sasiedzi += '@'
                except IndexError:
                    sasiedzi += ''
                try:
                    if dane[i-1][j] == '@':
                        sasiedzi += '@'
                except IndexError:
                    sasiedzi += ''
                try:
                    if dane[i-1][j+1] == '@':
                        sasiedzi += '@'
                except IndexError:
                    sasiedzi += ''
                if len(sasiedzi) < 4:
                    result += 1
    return result
            
def task_2(dane: list[list[str]]) -> int:
    result = 0
    warunek = True
    # robie buffer zone na okolo danych
    dane.insert(0, ['-'] * len(dane[0]))
    dane.append(['-'] * len(dane[0]))

    for i in range(len(dane)):
        dane[i].insert(0, '-')
        dane[i].append('-')
    #jak kod dziala to jest dobry pozdro    
    while warunek:
        idx = []
        temp = [row[:] for row in dane]
        for i in range(len(dane)):
            for j in range(len(dane[0])):
                sasiedzi = ''
                if dane[i][j] == '@':
                    try:
                        if dane[i+1][j-1] == '@':
                            sasiedzi += '@'
                    except IndexError:
                        sasiedzi += ''
                    try:
                        if dane[i+1][j] == '@':
                            sasiedzi += '@'
                    except IndexError:
                        sasiedzi += ''
                    try:
                        if dane[i+1][j+1] == '@':
                            sasiedzi += '@'
                    except IndexError:
                        sasiedzi += ''
                    try:
                        if dane[i][j-1] == '@':
                            sasiedzi += '@'
                    except IndexError:
                        sasiedzi += ''
                    try:
                        if dane[i][j+1] == '@':
                            sasiedzi += '@'
                    except IndexError:
                        sasiedzi += ''
                    try:
                        if dane[i-1][j-1] == '@':
                            sasiedzi += '@'
                    except IndexError:
                        sasiedzi += ''
                    try:
                        if dane[i-1][j] == '@':
                            sasiedzi += '@'
                    except IndexError:
                        sasiedzi += ''
                    try:
                        if dane[i-1][j+1] == '@':
                            sasiedzi += '@'
                    except IndexError:
                        sasiedzi += ''
                    if len(sasiedzi) < 4:
                        result += 1
                        idx.append([i, j])
        for idx in idx:
            dane[idx[0]][idx[1]] = 'x'
        wyn = []
        for n in range(len(dane)):
            if dane[n] == temp[n]:
                wyn.append(1)
            else:
                wyn.append(0)
        if len(set(wyn)) == 1 and wyn[0] == 1:
            warunek = False

    return result

def main() -> None:
    print(task_1(read_data('data/data4-example.txt')))
    print(task_1(read_data('data/data4.txt')))
    print(task_2(read_data('data/data4-example.txt')))
    print(task_2(read_data('data/data4.txt')))

if __name__ == '__main__':
    main()
