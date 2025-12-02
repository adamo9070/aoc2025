def read_data(file) -> list[str]:
    with open(file, 'r') as f:
        return f.read().strip().split(',')

def longest_substring(x: str) -> str:
    pass

# WARN: GOWNOGOWNOGOWNOGOWNOGOWNOGOWNO

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

def task_2(dane: list[str]) -> int: 
    dane2 = []
    result = 0
    for i in dane:
        dane2.append(i.strip().split('-'))
    for i in dane2:
        for n in range(int(i[0]), int(i[1])+1):
            if longest_substring(str(n)) == str(n)[0: len(longest_substring(str(n)))]:
                for k in range(len(longest_substring(str(n))), len(str(n)), len(longest_substring(str(n)))):
                    if str(n)[k:len(longest_substring(str(n)))] == longest_substring(str(n)):
                        result += n
    return result

print(longest_substring('112312'))
print(task_1(read_data('data/data1-example.txt')))
print(task_1(read_data('data/data1.txt')))
print('------task2--------')
print(task_2(read_data('data/data1-example.txt')))
print(task_2(read_data('data/data1.txt')))

