with open("input.txt", "r") as f:
    to_sum_all_file = []
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "five": 5,
        "four": 4,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }
    buffer = ""
    for line in f:
        for char in line: 
            buffer += char
            for key, values in numbers.items():
                if key in buffer:
                    buffer = buffer.replace(key, str(values)) + buffer[-1]
        print(buffer)
        to_add_each_line = []
        for char in buffer:
            if char.isdigit():
                to_add_each_line.append(char)
        line_add = to_add_each_line[0] + to_add_each_line[-1]
        to_sum_all_file.append(int(line_add))
        print(f"For this line : {line}, sum = {line_add}")
        buffer = ""
    sum(to_sum_all_file)
    print(f"Sum of all lines = {sum(to_sum_all_file)}")
