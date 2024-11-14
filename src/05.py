file_path = r'2020\input\05.txt'
id_list = []

def calculate_id(input : str) -> int:
    rows = list(range(128))
    columns = list(range(8))
    for letter in input:
            if letter == 'F':
                rows = rows[:int(len(rows)/2)]
            if letter == 'B':
                rows = rows[int(len(rows)/2):]
            if letter == 'L':
                columns = columns[:int(len(columns)/2)]
            if letter == 'R':
                columns = columns[int(len(columns)/2):]
    return rows[-1] * 8 + columns[-1]


def part_one() -> int:
    maximum_id = -1
    with open(file_path, 'r') as file:
         for line in file:
              #row = find_row(line[:7])
              #column = find_column(line[7:])
              id = calculate_id(line)
              id_list.append(id)
              if id > maximum_id:
                   maximum_id = id              
    print(maximum_id)
    return maximum_id 
    
        
def part_two() -> int:
    max = part_one()
    for id in range(0, max):
        if id not in id_list:
             if id+1 in id_list and id-1 in id_list:
                print(id)
                break
                
part_one()
part_two()