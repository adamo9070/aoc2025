def read_data(file: str) -> list[str]:
    with open(file, 'r') as F:
        return [z.strip() for z in F]

def task_1(data: list[str]) -> int:
    wazne = []
    wazne2 = []
    skladniki = []
    ile = 0
    for i in data:
        if i == '':
            wazne = data[:data.index(i)]
            skladniki = data[data.index(i) + 1:]
            break
    for i in range(len(wazne)):
        wazne2.append(wazne[i].split('-'))
    for i in skladniki:
        for j in wazne2:
            if int(j[0]) <= int(i) <= int(j[1]):
                ile += 1
                break
    return ile

def task_2(data: list[str]) -> int:
    wazne = []
    wazne2 = []
    ile = 0
    '''
    pomysl
    sprawdzac czy aktualne i[0] jest miedzy jakims innym i[0]-i[1] i zmienic range na taki zeby ich bylo mniej 
    '''
    for i in data:
        if i == '':
            wazne = data[:data.index(i)]
            break
    for i in range(len(wazne)):
        wazne2.append(wazne[i].split('-'))

    for i in range(len(wazne2)):
        for j in range(2):
            wazne2[i][j] = int(wazne2[i][j])

    wazne2 = sorted(wazne2, key=lambda x: x[0])
    
    # szukalem metody zeby wykonalo sie sensowna ilosc razy ale bez przesady
    while True:
        idx = 1
        temp_len = len(wazne2)
        for _ in range(len(wazne2)):
            a_start = wazne2[idx-1][0]
            a_end = wazne2[idx-1][1]
            b_start = wazne2[idx][0]
            b_end = wazne2[idx][1]
            # sprawdza czy sie overlapuja np a - [10, 30] b - [20, 25] --> [10, 30]
            if b_start >= a_start and b_end <= a_end:
                wazne2.pop(idx)
            # sprawdza czy b zaczyna sie w a i konczy poza nim np a - [10, 30] b - [15, 50] --> [10, 50]
            elif b_start <= a_end and b_end >= a_end:
                temp = [a_start, b_end]
                wazne2.pop(idx)
                wazne2.pop(idx-1)
                wazne2.insert(idx-1, temp)
            # innych opcji nie ma bo range sa posortowane wedlug idx 0 rosnaco
            idx += 1
            if idx > len(wazne2)-1:
                idx = 1
        if len(wazne2) == temp_len:
            break

    for i in wazne2:
        ile += abs(i[1] - i[0]) + 1
    return ile

def main() -> None:
    print(task_1(read_data('data/data5-example.txt')))
    print(task_1(read_data('data/data5.txt')))
    print(task_2(read_data('data/data5-example.txt')))
    print(task_2(read_data('data/data5.txt')))

if __name__ == '__main__':
    main()
