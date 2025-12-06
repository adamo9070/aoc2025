dane = [x.strip() for x in open('data/data6.txt')]
sumka = 0
pipi = []

for x in dane:
    t = []
    for char in x:
        t.append(char)
    pipi.append(t)

lili = []
numbers = []
symbols = []

for idx in range(0, len(pipi[0])):
    h = ''
    for row in range(0, len(pipi) - 1):
        h += pipi[row][idx]
    lili.append(h)

lili.append('    ')  # NIE ma mowy :sob: :sob:
t = []
while lili:
    if lili[0] != '    ':
        t.append(lili[0])
        lili.pop(0)
    else:
        numbers.append(t)
        t = []
        lili.pop(0)

tsym = pipi[-1]
while tsym:
    if tsym[0] in '+*':
        symbols.append(tsym[0])
        tsym.pop(0)
    else:
        tsym.pop(0)

for idx in range(0, len(symbols)):
    if symbols[idx] == '*':
        t = 1
        for num in numbers[idx]:
            t = t * int(num)
        sumka += t
    elif symbols[idx] == '+':
        for num in numbers[idx]:
            sumka += int(num)

print(sumka)