with open('Day 1/input.txt', 'r') as input_file:
    lines = input_file.readlines()

total_sum = 0

for line in lines:
    line.strip()
    for char in line:
        if char.isdigit():
            a = char
            break
    for char in line[::-1]:
         if char.isdigit():
            b = char
            break
    c = f'{a}{b}'
    total_sum += int(c)
    
print(total_sum)