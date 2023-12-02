game_data = {}

max_red_cubes = 12
max_green_cubes = 13
max_blue_cubes = 14

with open("AdventOfCode2023/DayTwo/input.txt", "r") as f:
    for line in f:
        split_line = line.split(": ")
        game_name = split_line[0]
        game_id = game_name[5:]
        split_games = split_line[1].split("; ")
        
        color_counts = {"red": 0, "green": 0, "blue": 0}
        
        for game in split_games:
            color_cubes = game.split(", ")
            
            for color_cube in color_cubes:
                count, color = color_cube.split(" ")
                color = color.rstrip("\n")
                color_counts[color] = max(color_counts[color], int(count))
        
        game_data[game_id] = color_counts

for game_id, color_counts in game_data.items():
    print(f"Game {game_id}: {color_counts}")


# Part 2
power_sum = 0

for game_id, color_counts in game_data.items():
    power = color_counts['red'] * color_counts['green'] * color_counts['blue']
    power_sum += power

print(f"Sum of products: {power_sum}")

# Part 1
game_data_copy = game_data.copy()

for game_id, color_counts in game_data_copy.items():
    if color_counts['red'] > max_red_cubes or color_counts['green'] > max_green_cubes or color_counts['blue'] > max_blue_cubes:
        del game_data[game_id]

game_id_sum = 0


for game_id, color_counts in game_data.items():
    print(f"Game {game_id}: {color_counts}")
    game_id_sum += int(game_id)

print(f"Sum of game IDs: {game_id_sum}")

