results = []

alphaNum = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

f = open(r'day1\input.txt')

def takeindex(elem):
    return elem[1]

for line in f.readlines():
    
    locs = []
    for char in line:
        if char.isdigit():
            index = line.find(char)
            locs.append([char, index])
            index2 = line.rfind(char)
            if index != index2:
                locs.append([char, index2])
            
    for i in alphaNum:
        if i in line:
            index = line.find(i)
            locs.append([alphaNum.index(i)+1, index])
            index2 = line.rfind(i)
            if index != index2:
                locs.append([alphaNum.index(i)+1, index2])

    locs.sort(key=takeindex)
    res = str(locs[0][0]) + str(locs[-1][0])
    results.append(int(res))

    
print(sum(results))
