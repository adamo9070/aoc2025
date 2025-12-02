def read_data(file) -> list[str]:
    with open(file, 'r') as f:
        return f.read().strip().split(',')

def longest_substring(x: str) -> str:
    l = 0
    l_max = 0
    max_s = 0
    sett = set()
    substring = ''

    for i in range(len(x)):
        while x[i] in sett:
            sett.remove(x[l])
            l += 1

        sett.add(x[i])
        if i - l + 1 > max_s:
            l_max = l
            max_s = i - l + 1
    substring = x[l_max:l_max + max_s]

    return substring

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

#print(longest_substring('112312'))
print(task_1(read_data('data/data1-example.txt')))
print(task_1(read_data('data/data1.txt')))

