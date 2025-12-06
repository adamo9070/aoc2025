inp = open('data.txt')
IDs = [x.split() for x in inp]
ranges = []
r2 = []

'''def bubel(l): #sorted() istnieje...
    i = len(l)
    while i > 0:
        for idx in range(0, i-1):
            if l[idx] > l[idx+1]:
                l[idx], l[idx+1] = l[idx+1], l[idx]
        i -= 1
    return l'''
        

while True:
    if IDs[0]:
        ranges.append(IDs[0])
        IDs.pop(0)
    else:
        IDs.pop(0)
        break

for r in ranges:
    for x in r:
        r2.append([int(y) for y in x.split('-')])
        
r2 = sorted(r2)
i=0
while i < len(r2)+2127:
    t = []
    for idx_r in range(0, len(r2)-1):
        if r2[idx_r][1] >= r2[idx_r+1][0]:
            t.append([r2[idx_r][0], r2[idx_r+1][1]])
        #elif r2[idx_r][0] > r2[idx_r+1][0] and r2[idx_r][1] > r2[idx_r+1][1]:
            #t.append([r2[idx_r][0], r2[idx_r][1]])
        else:
            t.append(r2[idx_r])
    if t:
        r2 = t
    i+=1

print(r2)
solution = r2[0][1] - r2[0][0] + 1
print(solution)