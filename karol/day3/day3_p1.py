ratings = [x.strip() for x in open('realne.txt')]
output_joltage = 0
 
for r in ratings:
    najw_idx = 0
    da_largest = 0  #https://www.youtube.com/watch?v=3QwZjhHcLZk
    lpj = ''
    for idx in range(0, len(r)):
        if int(r[idx]) > da_largest:
            najw_idx = idx
            da_largest = int(r[idx])
        #jeżeli jest ostatnia:
    if najw_idx == len(r)-1:
        lpj += str(da_largest)
        najw_idx, da_largest = 0, 0
        for idx in range(0, len(r)-1):
            if int(r[idx]) > da_largest:
                najw_idx, da_largest = idx, int(r[idx])
        lpj = str(da_largest) + lpj
    else:
        lpj += str(da_largest)
        x = najw_idx
        najw_idx, da_largest = 0, 0
        for idx in range(x+1, len(r)):
            if int(r[idx]) > da_largest:
                najw_idx = idx
                da_largest = int(r[idx])
        lpj = lpj + str(da_largest)
    output_joltage += int(lpj)

print(output_joltage)
