 
results = []

f = open(r'day1\input.txt')

for line in f.readlines():
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(char)

    res = numbers[0] + numbers[-1]
    results.append(int(res))  
    
print(results)
print(sum(results))

