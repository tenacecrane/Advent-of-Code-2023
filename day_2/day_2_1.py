# Read the input file
filepath = 'day_2/test_data.txt'
with open(filepath, 'r') as f:
    games = f.readlines()

for game in games:
    print(game)