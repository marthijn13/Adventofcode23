f = open('day2/input.txt')
results = []

for line in f.readlines():
    nr, content = line.split(':')
    possibility = content.split(';')
    print(possibility)
    red = 0
    green = 0
    blue = 0
    for option in possibility:
        colors = option.split(',')
        for color in colors:
            if 'red' in color:
                nRed = int(color[0:color.find('red')])
                if nRed > red:
                    red = nRed
            elif 'green' in color:
                nGreen = int(color[0:color.find('green')])
                if nGreen > green:
                    green = nGreen
            elif 'blue' in color:
                nBlue = int(color[0:color.find('blue')])
                if nBlue > blue:
                    blue = nBlue
    print("R: ", red, "G: ", green, "B: ", blue)
    results.append(red * green * blue)
print(results)
print(sum(results))