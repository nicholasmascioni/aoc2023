RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

'''
Data Structure Plan:

{
    Game # : [Max Red, Max Green, Max Blue]
}

The cubes are replaced after every draw, so the maximum number of cubes of each colour will
determine if the game was possible or not
'''

# Find the maximum number of each colour of cube drawn in each game
def find_colours(record: str) -> list[int]: 
    games = record.split(';')
    red_count = []
    green_count = []
    blue_count = []
    
    for game in games:     
        for item in game.split(','):
            if item.split()[1] == "red":
                red_count.append(int(item.split()[0]))
            if item.split()[1] == "green":
                green_count.append(int(item.split()[0]))
            if item.split()[1] == "blue":
                blue_count.append(int(item.split()[0]))
    
    return [max(red_count), max(green_count), max(blue_count)]

# Same as previous function but for finding the minimum number of cubes of each colour drawn
def get_min_colours(record: str) -> list[int]:
    games = record.split(';')
    red_count = []
    green_count = []
    blue_count = []
    
    for game in games:     
        for item in game.split(','):
            if item.split()[1] == "red":
                red_count.append(int(item.split()[0]))
            if item.split()[1] == "green":
                green_count.append(int(item.split()[0]))
            if item.split()[1] == "blue":
                blue_count.append(int(item.split()[0]))
    
    return [min(red_count), min(green_count), min(blue_count)]

def part1(input: list[str]) -> int:
    game_record = {}

    for line in input:
        record = line.split(':')
        game_id = record[0].split()
        game_record.update({int(game_id[1]) : find_colours(record[1])})

    possible_games = 0

    for game_number, cubes in game_record.items():
        print(game_number, cubes)
        if cubes[0] <= RED_MAX and cubes[1] <= GREEN_MAX and cubes[2] <= BLUE_MAX:
            possible_games += game_number
            
    return possible_games

def part2(input: list[str]) -> int:
    game_record = {}

    for line in input:
        record = line.split(':')
        game_id = record[0].split()
        game_record.update({int(game_id[1]) : find_colours(record[1])})

    power_sum = 0

    for _, cubes in game_record.items():
        power_sum += (cubes[0] * cubes[1] * cubes[2])

    return power_sum
            
            
def main() -> None:
    with open("inputs/day2.txt", 'r') as file:
        lines = [x.strip('\n') for x in file.readlines()]

    print(f"Part 1 solution: {part1(lines)}")
    print(f"Part 2 solution: {part2(lines)}")


if __name__ == "__main__":
    main()
    