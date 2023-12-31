MAX_CUBES = 39
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# Read the input file
filepath = 'day_2/data.txt'
with open(filepath, 'r') as f:
    games = f.readlines()

sum = 0

for game in games:
    game_id = int(game.split(' ')[1].split(':')[0])
    game = game.split(':')[1].strip()
    rounds = game.split(';')
    game_invalid = False
    # print(f"Game ID: {game_id}")
    # print(game)
    # print(rounds)
    for round in rounds:
        red_count = 0
        green_count = 0
        blue_count = 0
        colors = round.split(',')
        for color in colors:
            color = color.strip()
            if("red" in color):
                red_count += int(color.split(' ')[0])
            elif("green" in color):
                green_count += int(color.split(' ')[0])
            elif("blue" in color):
                blue_count += int(color.split(' ')[0])
        if((red_count + green_count + blue_count) > MAX_CUBES or red_count > MAX_RED or green_count > MAX_GREEN or blue_count > MAX_BLUE):
            game_invalid = True

    if(game_invalid is True):
        continue
    else:
        sum += game_id

print(sum)