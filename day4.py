'''
Plan:

Part 1:
Split by ':' and then by '|' to group card number, winning numbers, and your numbers
Check how many matches there are between winning numbers and your own by comparing the lists
Points for each card are 2^n-1 as long as n > 0, otherwise points are 0

{
    Card # : [[Winning Numbers], [Your Numbers]]
}

Part 2:
Store each card number with the corresponding number of copies and matches for that card in a dictionary
For each match that card has, add a number of copies of the next cards equal to the number of copies of
the current card

{
    Card # : [Copies (initially 1) , Matches]
}
'''

def part1(input: list[str]) -> int:
    scratch_cards = {}
    scores = []

    for line in input:
        scratch_cards.update({int(line.split(':')[0].split()[1]) : [[int(x) for x in line.split(':')[1].split('|')[0].split()] , 
                                                                    [int(x) for x in line.split(':')[1].split('|')[1].split()]]})
        
    for _, numbers in scratch_cards.items():
        matches = 0
        winning_numbers = numbers[0]
        your_numbers = numbers[1]

        for num in your_numbers:
            if num in winning_numbers:
                matches += 1
        
        if matches > 0:
            scores.append(2**(matches-1))

    return sum(scores)


def part2(input: list[str]) -> int:
    scratch_cards = {}
    card_totals = {}

    for line in input:
        scratch_cards.update({int(line.split(':')[0].split()[1]) : [[int(x) for x in line.split(':')[1].split('|')[0].split()] , 
                                                                    [int(x) for x in line.split(':')[1].split('|')[1].split()]]})
    
    card_totals = {x : [1] for x in scratch_cards}  # Each total starts at 1 (no copies at first, besides the original card)

    # Finish constructing card_totals dictionary
    for card_num, numbers in scratch_cards.items():
        matches = 0
        winning_numbers = numbers[0]
        your_numbers = numbers[1]

        for num in your_numbers:
            if num in winning_numbers:
                matches += 1

        card_totals[card_num].append(matches)
        
    total_copies = 0

    for num, elements in card_totals.items():
        copies = elements[0]
        matches = elements[1]

        print(f"*** Card: {num} Copies: {copies} Matches: {matches} ***")

        for i in range(0, matches):
            print(f"Card {num+i+1} getting {copies} more copies!")
            card_totals[num+i+1][0] += copies

        total_copies += card_totals[num][0]

    return total_copies
        

def main() -> None:
    with open("inputs/day4.txt", 'r') as file:
        lines = [x.strip('\n') for x in file.readlines()]

    print(f"Part 1 solution: {part1(lines)}")
    print(f"Part 2 solution: {part2(lines)}")


if __name__ == "__main__":
    main()
