def read_data(file) -> list[str]:
    with open(file, 'r') as f:
        return f.read().strip().split(',')

def dzielniki(x: str) -> list[int]:
    dzielniki = []
    for i in range(1, int(x)):
        if len(x) % i == 0:
            dzielniki.append(i)
    return dzielniki

def task_1(dane: list[str]) -> int:
    dane2 = []
    result = 0
    for i in dane:
        dane2.append(i.strip().split('-'))
    for i in dane2:
        for n in range(int(i[0]), int(i[1])+1):
            j = len(str(n)) // 2
            if str(n)[j:] == str(n)[:j]:
                result += n
    return result

# Ściągnięte od karola pozdro 600 100 900
def task_2(dane: list[str]) -> int: 
    dane2 = []
    results = []
    for i in dane:
        dane2.append(i.strip().split('-'))
    for i in dane2:
        for n in range(int(i[0]), int(i[1])+1):
            for dz in range(1, len(str(n))):
                if len(str(n)) % dz == 0:
                    fragmenty = [str(n)[i:i + dz] for i in range(0, len(str(n)), dz)]
                    if len(set(fragmenty)) == 1:
                        results.append(n)
    return sum(set(results))

print(task_1(read_data('data/data1-example.txt')))
print(task_1(read_data('data/data1.txt')))
print('------task2--------')
print(task_2(read_data('data/data1-example.txt')))
print(task_2(read_data('data/data1.txt')))

