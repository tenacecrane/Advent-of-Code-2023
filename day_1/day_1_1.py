# Day 1 Part 1

def sum_all_inputs():

    # Read the input file
    filepath = 'day_1/data.txt'
    with open(filepath, 'r') as f:
        inputs = f.readlines()

    sum = 0
    num_array = []

    # I feel like this way of doing it is embarassing LOL but it's midnight
    # and Alexa wants me to go to sleep had to go FAST not pretty.
    for string in inputs:
        for char in range(len(string)):
            try:
                num_array.append(int(string[char]))
            except:
                continue
        if len(num_array) > 1:
            number_to_add = int((str(num_array[0]) + str(num_array[len(num_array)-1])))
            sum += number_to_add
        elif len(num_array) == 1:
            number_to_add = int((str(num_array[0]) + str(num_array[0])))
            sum += number_to_add
        num_array = []

    print(sum)

sum_all_inputs()