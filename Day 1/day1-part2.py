with open('Day 1/input.txt', 'r') as input_file:
    lines = input_file.readlines()
    
total_sum = 0

digits = {'one':'one1one','two':'two2two', 'three':'three3three', 'four':'four4four', 'five':'five5five', 'six':'six6six', 'seven':'seven7seven', 'eight':'eight8eight', 'nine':'nine9nine'}
for line in lines:
    line = line.strip()
    for letter, digit in digits.items():
        line = line.replace(letter, digit)        
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