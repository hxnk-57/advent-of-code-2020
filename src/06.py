file_path = r"2020\input\06-test.txt"

def part_one() -> int:
    groups = []
    content = ""
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line:
                content+= line
            else:
                groups.append(content)
                print(content)
                content = ""
        if content:
            groups.append(content)

    total = 0
    for group in groups:
        questions = "abcdefghiklmnopqrstuvwxyz"
        group_total = 0
        for letter in group:
            if letter in questions:
                questions = questions.strip(letter)
                print(questions)
                group_total += 1
        total += group_total
        print(group_total)


def part_two() -> int:
    print("bruh")

part_one()
part_two()