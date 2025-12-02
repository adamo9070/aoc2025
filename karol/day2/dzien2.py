inp = open('input.txt').readlines()[0]
dane = inp.split(',')
ranges = [x.split('-') for x in dane]
sum_of_invalid = 0

for r in ranges:
    for ID in range(int(r[0]), int(r[1])+1):
        p = len(str(ID))
        if str(ID)[0] == '0':
            sum_of_invalid += ID
        elif p % 2 == 0:
            t = int(p/2)
            if str(ID)[t:] == str(ID)[:t]:
                sum_of_invalid += ID

print(sum_of_invalid)
