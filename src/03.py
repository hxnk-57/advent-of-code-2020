file_path : str = r"2020\input\03.txt"

def part_one() -> int:
    trees = 0
    square = 0
    file = open(file_path, 'r').read().splitlines()
    for line in file:
        square = square % len(line)
        if (line[square]=='#'):
            trees += 1
        square += 3

    print(f"There are {trees} trees")


def part_two() -> int:

    slopes = [
        {"right": 1, "down": 1, "trees": 0},
        {"right": 3, "down": 1, "trees": 0},
        {"right": 5, "down": 1, "trees": 0},
        {"right": 7, "down": 1, "trees": 0},
        {"right": 1, "down": 2, "trees": 0},
    ]

    product = 1
    for slope in slopes:
        file = open(file_path, 'r').read().splitlines()
        square = 0  
        for i, line in enumerate(file):
            square = square % len(line)
            if i % slope["down"] == 0:
                if (line[square]=='#'):
                    slope["trees"] += 1
                square += slope["right"]
        product *= slope["trees"]
    print(product)
     
part_one()
part_two()