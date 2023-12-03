import string

with open("AdventOfCode2023/DayThree/test.txt", "r") as f:
    lines = []
    for line in f:
        lines.append(line)

# Select numbers from each line that are next to symbols (not dots).
# symbols can be next to the number on the left or right side.
# symbols can be one the previous or next line up, down or diagonal.

# 1. Find the numbers that are next to symbols on the same line.


# 2. Find the numbers that are next to symbols on the previous line.
# 3. Find the numbers that are next to symbols on the next line.
def get_numbers_from_line(line):
    char_position = 0
    complete_numbers_positions = []
    symbols_positions = []
    while char_position < len(line):
        char = line[char_position]
        start_position = char_position
        if char.isdigit():
            complete_number = ""
            while char.isdigit():
                complete_number += str(char)
                char_position += 1
                if char_position < len(line):
                    char = line[char_position]
            if complete_number:
                end_position = char_position - 1
                complete_numbers_positions.append(
                    (complete_number, start_position, end_position)
                )
        elif char == "*" and char in string.punctuation:
            symbols_positions.append((char, start_position-1, start_position+1))
            char_position += 1
        else:
            char_position += 1
    return complete_numbers_positions, symbols_positions


def compare_lines(prev_line, curr_line, next_line):
    curr_numbers, curr_symbols = get_numbers_from_line(curr_line)
    prev_numbers, prev_symbols = (
        get_numbers_from_line(prev_line) if prev_line else ([], [])
    )
    next_numbers, next_symbols = (
        get_numbers_from_line(next_line) if next_line else ([], [])
    )
    
    gear_numbers = 0
    for number, start, end in curr_numbers:
        symbol_in_prev_line = any(sym_start <= start <= sym_end or sym_start <= end <= sym_end for symbol, sym_start, sym_end in prev_symbols)
        symbol_in_next_line = any(sym_start <= start <= sym_end or sym_start <= end <= sym_end for symbol, sym_start, sym_end in next_symbols)
        symbol_next_to_number = any(sym_end == start or sym_start == end for symbol, sym_start, sym_end in curr_symbols)
        adjacent_numbers = [num for num, num_start, num_end in curr_numbers if num_start == end + 1 or num_end == start - 1]
        if symbol_in_prev_line or symbol_in_next_line or symbol_next_to_number and len(adjacent_numbers) == 2:
            # print(f"For number {number}, yes")
            gear_numbers = number
        else:
            pass
            # print(f"For number {number}, no")
    return gear_numbers

gear_numbers = []
total_sum = 0
for i in range(len(lines)):
    prev_line = lines[i - 1] if i - 1 >= 0 else None
    next_line = lines[i + 1] if i + 1 < len(lines) else None
    if compare_lines(prev_line, lines[i], next_line) != 0:
        gear_numbers.append(int(compare_lines(prev_line, lines[i], next_line)))

gear_numbers = [gear_numbers[i] * gear_numbers[i + 1] for i in range(0, len(gear_numbers), 2)]
total_sum = sum(gear_numbers)

print(f"Total sum: {total_sum}")