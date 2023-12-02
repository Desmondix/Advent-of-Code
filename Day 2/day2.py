with open('Day 2/input.txt', 'r') as f:
    lines = f.readlines()


target = {"red":12, "green":13, "blue":14}
somma = 0
for line in lines:
    game_str, pull_str = line.split(": ")
    game_id = int(game_str.split(" ")[-1])
    game_valid = True
    for pull in pull_str.split("; "):
        for color in pull.split(", "):
            color_num, color_str = color.strip().split(" ")
            num = int(color_num)
            if(target[color_str] < num):
                game_valid = False
    if(game_valid):
        somma += game_id
print(somma)       