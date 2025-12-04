inp = open('input.txt').readlines()[0]
dane = inp.split(',')
ranges = [x.split('-') for x in dane]
invalid_IDs = []

for r in ranges:
    for ID in range(int(r[0]), int(r[1])+1):
        dł = len(str(ID))
        #dzielniki dł
        for dz in range(1, dł):
            if dł%dz == 0:
                #dzielenie ID na kawałki o len == dz
                slices = [str(ID)[i:i+dz] for i in range(0, dł, dz)]
                if len(set(slices)) == 1:
                    invalid_IDs.append(ID)
                        

print(sum(set(invalid_IDs)))
