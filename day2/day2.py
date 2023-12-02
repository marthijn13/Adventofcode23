f = open('day2/input.txt')
results = []

for line in f.readlines():
    nr, content = line.split(':')
    possibility = content.split(';')
    print(possibility)
    for option in possibility:
        colors = option.split(',')
        print(colors)
        valid = True
        for color in colors:
            if 'red' in color and valid:
                valid = int(color[0:color.find('red')]) <= 12
            elif 'green' in color and valid:
                valid = int(color[0:color.find('green')]) <= 13
            elif 'blue' in color and valid:
                valid = int(color[0:color.find('blue')]) <= 14
        if not valid:
            break
    if valid:
        results.append(int(nr[5:]))
print(results)
print(sum(results))
        



