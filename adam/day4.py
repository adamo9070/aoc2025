def read_data(file: str) -> list[str]:
    with open(file, 'r') as F:
        return [z.strip() for z in F]

def task_1(dane: list[str]):
    result = 0
    # robie buffer zone na okolo danych
    dane.insert(0, 'x' * len(dane[0]))
    dane.append('x' * len(dane[0]))

    for i in range(len(dane)):
        dane[i] = 'x' + dane[i] + 'x'
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
            

def main() -> None:
    print(task_1(read_data('data/data4-example.txt')))
    print(task_1(read_data('data/data4.txt')))

if __name__ == '__main__':
    main()
