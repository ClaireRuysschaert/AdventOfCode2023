# Day Four Advent of Code 2023

with open("AdventOfCode2023/DayFour/input.txt", "r") as f:
    lines = []
    for line in f:
        line = line.replace("\n", "")
        lines.append(line)

# separate line ":" and |
sum_values = 0
for line in lines:
    line = line.split(": ")
    winning_numbers = line[1].split(" | ")[0]
    numbers_to_check = line[1].split(" | ")[1]
    # store in a list winning number 2 numbers by 2 numbers str to int
    # avoid blank space 
    winning_numbers = winning_numbers.split(" ")
    numbers_to_check = numbers_to_check.split(" ")
    winning_numbers = [num for num in winning_numbers if num]
    numbers_to_check = [num for num in numbers_to_check if num]
    
    #check if numbers_to_check are in winning_numbers
    count = 0
    value = 1
    for num in numbers_to_check:
        if num not in winning_numbers:
            pass
        else:
            count += 1
    if count == 0:
        value = 0
    else:
        value = pow(2, count-1)
    
    sum_values += int(value)
    print(f"Value : {value}, count : {count}")
    print(sum_values)

print(sum_values)
