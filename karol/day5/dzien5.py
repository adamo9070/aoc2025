inp = open('data.txt')
IDs = [x.split() for x in inp]
ranges = []
fresh = []

while True:
    if IDs[0]:
        ranges.append(IDs[0])
        IDs.pop(0)
    else:
        IDs.pop(0)
        break

for r in ranges:
    t = r[0].split('-')
    p, k = int(t[0]), int(t[1]) #fresh id range
    for ingredient in IDs:
        i = int(ingredient[0])
        if i in range(p, k+1):
            fresh.append(i)

print(len(set(fresh)))