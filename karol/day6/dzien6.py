dane = [ x.split() for x in open('data.txt')]
sumka = 0

for idx in range(0, len(dane[0])):
    if dane[-1][idx] == '+':
        for row in range(0, len(dane)-1):
            num = int(dane[row][idx])
            sumka += num
    else:
        t = 1
        for row in range(0, len(dane)-1):
            num = int(dane[row][idx])
            t = t*num
        sumka += t
        
print(sumka)