# Day 1 Part 2

num_dictionary = {"zero":0, "one":1,"two":2,"three":3,"four":4,"five":5,"six":6, "seven":7, "eight":8,"nine":9}
num_words = []
for key in num_dictionary:
     num_words.append(key)

def get_first_number(string):
        num_word = ''
        for c in string:
            if(c.isnumeric()):
                return int(c)
            else:
                num_word += c
                for word in num_words:
                    if word in num_word:
                        return num_dictionary[word]

def get_last_number(string):
    num_word = ''
    for c in string[::-1]:
        if(c.isnumeric()):
            return int(c)
        else:
            num_word = c + num_word
            for word in num_words:
                if word in num_word:
                    return num_dictionary[word]

def sum_all_inputs_including_words():
    sum = 0

    # Read the input file
    filepath = 'day_1/data.txt'
    with open(filepath, 'r') as f:
        inputs = f.readlines()

    for string in inputs:
        # Strip newline characters
        string = string.strip()
        # combine the first and last numbers into one number
        sum += int(str(get_first_number(string)) + str(get_last_number(string)))
    print(sum)

sum_all_inputs_including_words()