with open('Day 2/input.txt', 'r') as f:
    lines = f.readlines()

somma = 0
for line in lines:
    red = 0
    green = 0
    blue = 0
    game_str, pull_str = line.split(": ")
    pull_str = pull_str.replace(";","")
    pull_str = pull_str.replace(",","")
    x = pull_str.strip().split(" ")
    for index, elem in enumerate(x):
        if elem == 'green':
            if int(x[index-1]) > green:
                green = int(x[index-1])
        if elem == 'red':
            if int(x[index-1]) > red:
                red = int(x[index-1])
        if elem == 'blue':
            if int(x[index-1]) > blue:
                blue = int(x[index-1])
    power = green*red*blue
    somma += power

print(somma) 

        
