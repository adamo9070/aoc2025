'''
https://i.imgflip.com/7ik090.jpg <- me rn
nie wiem co jeszcze moge zmienić żeby było dobrze :(
próbowałem w róznych miejscach naliczać sol2 (%100 też) no i idk
jeśli to czytasz i masz tipa to jakby.... sharepls..... jutro skończę (może)
'''

dane = [x.strip() for x in open('dane.txt')]
p = 50
sol, sol2 = 0, 0

for ins in dane:
    prev = p
    if ins[:1] == 'L':
        rot = int(ins[1:])
        p -= rot%100
        if p < 0:
            sol2 += 1
            p = 99 + p + 1
    else:
        rot = int(ins[1:])
        p += rot%100
        if p > 99:
            sol2 += 1
            p = abs(99 - p + 1)
    sol2 += rot//99
    #if (ins[:1] == 'L' and prev < p) or (ins[:1] == 'R' and prev > p):
        #sol2 += 1 + rot//99
    if p == 0:
        sol += 1

print(f'part 1: {sol}\npart 2: {sol2}')
