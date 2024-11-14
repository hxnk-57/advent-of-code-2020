import re

pattern = r"(\d+)-(\d+) (\w): (.+)"
file_path : str = r"2020\input\02.txt"

def part_one() -> int:
    valid_passwords : int = 0
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            minimum = int(match.group(1))
            maximum = int(match.group(2))
            letter = match.group(3)
            password = match.group(4)
            count = 0
            for character in password:
                if character == letter:
                    count += 1
            if count <= maximum and count >= minimum:
                valid_passwords += 1
    file.close()
    print(valid_passwords)


def part_two() -> int:
    valid_passwords : int = 0
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            minimum = int(match.group(1))
            maximum = int(match.group(2))
            letter = match.group(3)
            password = match.group(4)
            if maximum-1 < len(password):
                if (password[minimum-1] == letter) ^ (password[maximum-1] == letter):
                    valid_passwords += 1
    file.close()
    print(valid_passwords)

part_one()
part_two()