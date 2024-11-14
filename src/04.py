import re
file_path = r"2020\input\04.txt"


def contains_all_fields(passport : str) -> bool:
    required_fields = ["ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:"]
    for field in required_fields:
        if field not in passport:
            return False
    return True

def is_valid(passport : str) -> bool:
    byr_pattern = r'byr:(\d{4})'
    iyr_pattern = r'iyr:(\d{4})'
    eyr_pattern = r'eyr:(\d{4})'
    ecl_pattern = r'ecl:amb|ecl:blu|ecl:brn|ecl:gry|ecl:grn|ecl:hzl|ecl:oth'
    pid_pattern = r'pid:(\d{9})'
    hcl_pattern = r'#[0-9a-f]{6}'
    
    byr = int(re.search(byr_pattern, passport).group(1))
    if byr < 1920 or byr > 2002:
        return False
    iyr = int(re.search(iyr_pattern, passport).group(1))
    if iyr < 2010 or iyr > 2020:
        return False
    eyr = int(re.search(eyr_pattern, passport).group(1))
    if eyr < 2020 or eyr > 2030:
        return False
    cm = re.search(r'\d+cm', passport) 
    inch = re.search(r'\d+in',passport)
    if not (cm or inch):
        return False
    if cm:
        if int(cm.group()[:-2]) < 150 or int(cm.group()[:-2]) > 193:
            return False
    if inch:
        if int(inch.group()[:-2]) < 59 or int(inch.group()[:-2]) > 76:
            return False 
    ecl =  re.search(ecl_pattern, passport)  
    if not ecl:
         return False
    ecl =  re.search(ecl_pattern, passport).group()
    pid = re.search(pid_pattern, passport)
    if not pid:
        return False
    pid = re.search(pid_pattern, passport).group()
    hcl = re.search(hcl_pattern, passport)
    if not hcl:
        return False
    hcl = re.search(hcl_pattern, passport).group()
    print(f"""
    byr:{byr}
    iyr:{iyr}
    eyr:{eyr}
    hgt:{cm, inch}
    hcl:{hcl}
    ecl:{ecl}
    pid:{pid, len(pid)-4}
""")
    #input('Press Enter to continue...')
    return True
      

def part_one() -> int:
    valid_passports = 0
    passport = ""
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                passport += line
            else:
                if contains_all_fields(passport):
                    valid_passports += 1
                passport = ""
        if passport and contains_all_fields(passport):
            valid_passports += 1
                    
    print(valid_passports)


def part_two() -> int:
    valid_passports = 0
    passport = ""
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                passport += line
            else:
                if contains_all_fields(passport) and is_valid(passport):
                    valid_passports += 1
                passport = ""
        if passport and contains_all_fields(passport) and is_valid(passport):
            valid_passports += 1
                    
    print(valid_passports)

#part_one()
part_two()