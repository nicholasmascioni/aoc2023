def part1(lines: list[str]) -> int:
    values = []

    for line in lines:
        numbers = []
        for char in line:
            if char.isdigit():
                numbers.append(int(char))
        values.append((numbers[0] * 10) + numbers[-1])
    
    return sum(values)


def part2(lines: list[str]) -> int:
    # Map words to the corresponding numbers
    digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    values = []

    for line in lines:
        buffer = ""
        numbers = []

        for char in line:
            if char.isdigit():
                numbers.append(int(char))
            else:
                buffer += char
                for digit in digits:
                    if digit in buffer:
                        numbers.append(int(digits.get(digit)))
                        buffer = buffer[-1]  # Keep the last character in the buffer to deal with overlap
                        break
                
        values.append((numbers[0] * 10) + numbers[-1])

    return sum(values)


def main() -> None:
    with open("inputs/day1.txt", 'r') as file:
        lines = [x.strip('\n') for x in file.readlines()]

    print(f"Part 1 solution: {part1(lines)}")
    print(f"Part 2 solution: {part2(lines)}")


if __name__ == "__main__":
    main()
