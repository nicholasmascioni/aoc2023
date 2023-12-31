'''
Plan:

Part 1:
Store input in a list of strings, create function to determine if any numbers are adjacent to a given point in the grid
Iterate through all points in the grid searching for characters which are not numbers or periods
If adjacent number is found, parse the string which contains it to extract the whole number, then append to a list
Return the sum of the list 

Part 2:
Similar function to search for adjacent numbers, but only searching for * where there are exactly 2 adjacent numbers
Once the coordinates are found, the find_number function can be used to determine the actual numbers and multiply
them together, append the sum to a list and then return the sum of all values in the list
''' 

# Check for symbols which have numbers adjacent to them and return the rows and columns of those numbers
def is_adjacent(row: int, col: int, arr: list[str]) -> list[tuple[int, int]]:
    coordinates = []
    # Only check symbols
    if arr[row][col] != '.' and not arr[row][col].isdigit(): 

        # Check top-left corner 
        if row == 0 and col == 0:
            print("Top left corner", arr[row][col])

            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row+1][col+1].isdigit():
                print("Right diagonal!", arr[row+1][col+1])
                coordinates.append((row+1, col+1))

        # Check top-right corner
        elif row == 0 and col == len(arr[0])-1:
            print("Top right corner", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row+1][col-1].isdigit():
                print("Left diagonal!", arr[row+1][col-1])
                coordinates.append((row+1, col-1))

        # Check bottom-left corner
        elif row == len(arr)-1 and col == 0:
            print("Bottom left corner", arr[row][col])

            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row-1][col+1].isdigit():
                print("Right diagonal!", arr[row-1][col+1])
                coordinates.append((row-1, col+1))

        # Check bottom-right corner
        elif row == len(arr)-1 and col == len(arr[0])-1:
            print("Bottom right corner", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row-1][col-1].isdigit():
                print("Right diagonal!", arr[row-1][col-1])
                coordinates.append((row-1, col-1))
            
        # Check first row (no corners)
        elif row == 0 and col != 0 and col != len(arr[0])-1:
            print("First row", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row+1][col-1].isdigit():
                print("Left diagonal!", arr[row+1][col-1])
                coordinates.append((row+1, col-1))
            if arr[row+1][col+1].isdigit():
                print("Right diagonal!", arr[row+1][col+1])
                coordinates.append((row+1, col+1))

        # Check last row (no corners)
        elif row == len(arr)-1 and col != 0 and col != len(arr[0])-1:
            print("Last row", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row-1][col-1].isdigit():
                print("Left diagonal!", arr[row-1][col-1])
                coordinates.append((row-1, col-1))
            if arr[row-1][col+1].isdigit():
                print("Right diagonal!", arr[row-1][col+1])
                coordinates.append((row-1, col+1))

        # Check first column (no corners)
        elif col == 0 and row != 0 and row != len(arr)-1:
            print("First column", arr[row][col])

            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row-1][col+1].isdigit():
                print("Up right diagonal!", arr[row-1][col+1])
                coordinates.append((row-1, col+1))
            if arr[row+1][col+1].isdigit():
                print("Down right diagonal!", arr[row+1][col+1])
                coordinates.append((row+1, col+1))

        # Check last column (no corners)
        elif col == len(arr[0])-1 and row != 0 and row != len(arr)-1:
            print("Last column", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row-1][col-1].isdigit():
                print("Up left diagonal!", arr[row-1][col-1])
                coordinates.append((row-1, col-1))
            if arr[row+1][col-1].isdigit():
                print("Down left diagonal!", arr[row+1][col-1])
                coordinates.append((row+1, col-1))

        # Inside the outer edge
        else:
            print("Inside", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row-1][col-1].isdigit():
                print("Up left diagonal!", arr[row-1][col-1])
                coordinates.append((row-1, col-1))
            if arr[row-1][col+1].isdigit():
                print("Up right diagonal!", arr[row-1][col+1])
                coordinates.append((row-1, col+1))
            if arr[row+1][col-1].isdigit():
                print("Down left diagonal!", arr[row+1][col-1])
                coordinates.append((row+1, col-1))
            if arr[row+1][col+1].isdigit():
                print("Down right diagonal!", arr[row+1][col+1])
                coordinates.append((row+1, col+1))

    return coordinates


# Same as is_adjacent but only checks for *
def is_gear(row: int, col: int, arr: list[str]) -> list[tuple[int, int]]:
    coordinates = []
    # Only check *
    if arr[row][col] == '*': 

        # Check top-left corner 
        if row == 0 and col == 0:
            print("Top left corner", arr[row][col])

            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row+1][col+1].isdigit():
                print("Right diagonal!", arr[row+1][col+1])
                coordinates.append((row+1, col+1))

        # Check top-right corner
        elif row == 0 and col == len(arr[0])-1:
            print("Top right corner", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row+1][col-1].isdigit():
                print("Left diagonal!", arr[row+1][col-1])
                coordinates.append((row+1, col-1))

        # Check bottom-left corner
        elif row == len(arr)-1 and col == 0:
            print("Bottom left corner", arr[row][col])

            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row-1][col+1].isdigit():
                print("Right diagonal!", arr[row-1][col+1])
                coordinates.append((row-1, col+1))

        # Check bottom-right corner
        elif row == len(arr)-1 and col == len(arr[0])-1:
            print("Bottom right corner", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row-1][col-1].isdigit():
                print("Right diagonal!", arr[row-1][col-1])
                coordinates.append((row-1, col-1))
            
        # Check first row (no corners)
        elif row == 0 and col != 0 and col != len(arr[0])-1:
            print("First row", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row+1][col-1].isdigit():
                print("Left diagonal!", arr[row+1][col-1])
                coordinates.append((row+1, col-1))
            if arr[row+1][col+1].isdigit():
                print("Right diagonal!", arr[row+1][col+1])
                coordinates.append((row+1, col+1))

        # Check last row (no corners)
        elif row == len(arr)-1 and col != 0 and col != len(arr[0])-1:
            print("Last row", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row-1][col-1].isdigit():
                print("Left diagonal!", arr[row-1][col-1])
                coordinates.append((row-1, col-1))
            if arr[row-1][col+1].isdigit():
                print("Right diagonal!", arr[row-1][col+1])
                coordinates.append((row-1, col+1))

        # Check first column (no corners)
        elif col == 0 and row != 0 and row != len(arr)-1:
            print("First column", arr[row][col])

            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row-1][col+1].isdigit():
                print("Up right diagonal!", arr[row-1][col+1])
                coordinates.append((row-1, col+1))
            if arr[row+1][col+1].isdigit():
                print("Down right diagonal!", arr[row+1][col+1])
                coordinates.append((row+1, col+1))

        # Check last column (no corners)
        elif col == len(arr[0])-1 and row != 0 and row != len(arr)-1:
            print("Last column", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row-1][col-1].isdigit():
                print("Up left diagonal!", arr[row-1][col-1])
                coordinates.append((row-1, col-1))
            if arr[row+1][col-1].isdigit():
                print("Down left diagonal!", arr[row+1][col-1])
                coordinates.append((row+1, col-1))

        # Inside the outer edge
        else:
            print("Inside", arr[row][col])

            if arr[row][col-1].isdigit():
                print("To the left!", arr[row][col-1])
                coordinates.append((row, col-1))
            if arr[row][col+1].isdigit():
                print("To the right!", arr[row][col+1])
                coordinates.append((row, col+1))
            if arr[row-1][col].isdigit():
                print("Above!", arr[row-1][col])
                coordinates.append((row-1, col))
            if arr[row+1][col].isdigit():
                print("Below!", arr[row+1][col])
                coordinates.append((row+1, col))
            if arr[row-1][col-1].isdigit():
                print("Up left diagonal!", arr[row-1][col-1])
                coordinates.append((row-1, col-1))
            if arr[row-1][col+1].isdigit():
                print("Up right diagonal!", arr[row-1][col+1])
                coordinates.append((row-1, col+1))
            if arr[row+1][col-1].isdigit():
                print("Down left diagonal!", arr[row+1][col-1])
                coordinates.append((row+1, col-1))
            if arr[row+1][col+1].isdigit():
                print("Down right diagonal!", arr[row+1][col+1])
                coordinates.append((row+1, col+1))

    return coordinates

# Given the x and y coordinate of a number, go as far left as possible in the row
# Either hitting a '.' or the start of the row, and then go right to determine the 
# whole number adjacent to the symbol
def find_number(coordinates: list[tuple[int, int]], arr: list[str]) -> list[int]:
    numbers = []
    explored = []  # Keep track of visited coordinates to avoid duplicate numbers

    for pair in coordinates:
        row = pair[0]
        col = pair[1]

        # Find leftmost and rightmost indices of number
        left = col
        right = col

        while left >= 0 and arr[row][left].isdigit():
            left -= 1

        while right < len(arr[0]) and arr[row][right].isdigit():
            right += 1
        
        if (row, left+1, right-1) not in explored:
            numbers.append(int(arr[row][left+1:right]))

        explored.append((row, left+1, right-1))

    return numbers


# Same as find number but will only return numbers which are part of valid gear ratios
def find_gear(coordinates: list[tuple[int, int]], arr: list[str]) -> int:
    numbers = []
    explored = []  # Keep track of visited coordinates to avoid duplicate numbers

    for pair in coordinates:
        row = pair[0]
        col = pair[1]

        # Find leftmost and rightmost indices of number
        left = col
        right = col

        while left >= 0 and arr[row][left].isdigit():
            left -= 1

        while right < len(arr[0]) and arr[row][right].isdigit():
            right += 1
        
        if (row, left+1, right-1) not in explored:
            numbers.append(int(arr[row][left+1:right]))

        explored.append((row, left+1, right-1))

    if len(numbers) == 2:  # For a gear to be valid, it must have exactly 2 adjacent numbers
        return numbers[0] * numbers[1]
    
    return 0


def part1(input: list[str]) -> int:
    board = []
    coordinates = []
    part_numbers = []

    for line in input:
        board.append(line)

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            coordinates.extend(is_adjacent(i, j, board))

    part_numbers = find_number(coordinates, board)

    return sum(part_numbers)


def part2(input: list[str]) -> int:
    board = []
    coordinates = []
    gear_ratios = []

    for line in input:
        board.append(line)

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            coordinates.append(is_gear(i, j, board))  # Using a 2D list this time to seperate coordinates by each gear

    for coordinate in coordinates:
        if len(coordinate) != 0:  # Handle empty lists
            gear_ratios.append(find_gear(coordinate, board))

    return sum(gear_ratios)

    
def main() -> None:
    with open("inputs/day3.txt", 'r') as file:
        lines = [x.strip('\n') for x in file.readlines()]

    print(f"Part 1 solution: {part1(lines)}")
    print(f"Part 2 solution: {part2(lines)}")

if __name__ == "__main__":
    main()
