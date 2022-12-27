# The following code (unless otherwise stated) is used for both parts of Day 3
with open('puzzle3.txt', 'r') as filename:
    lines = filename.readlines()

no_newline_list = []

for element in lines:
    removed_newlines = element.split('\n')
    if '' in removed_newlines:
        removed_newlines.remove('')
    no_newline_list.append(removed_newlines)

# print(no_newline_list)

priorities = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

# The following code (unless otherwise stated) is used for Day 3 Part 2

every_third = 1

list_groups = []
group_list = []
for rucksack_list in no_newline_list:
    if every_third % 3 != 0:
        group_list.append(rucksack_list)
        every_third += 1
    else:
        group_list.append(rucksack_list)
        list_groups.append(group_list)
        group_list = []
        every_third += 1

# print(list_groups)

current_group = []
added_member = 0
group_badges = []

for group_list in list_groups:
    not_found_yet = True
    for member_list in group_list:
        added_member += 1
        for items in member_list:
            current_group.append(items)
        # print(added_member)
        if added_member == 3:
            # print(f"current group: {current_group}")
            for item in items:
                if (item in current_group[0]) and (item in current_group[1]) and (item in current_group[2]) and (not_found_yet == True):
                    group_badges.append(item)
                    not_found_yet = False
                    # print('added')
        
        # for items in member_list:
            
        #for items in member_list:
         #   for item in items:
    # print(current_group)
    # for 
    current_group = []
    added_member = 0

# print(group_badges)

sum_priorities = 0
for item in group_badges:
    sum_priorities += priorities[item]

print(sum_priorities) # Answer: 2821

# The following code (unless otherwise stated) is used for Day 3 Part 1
'''first_compartment = []
second_compartment = []
duplicates = []
current_num = 0
final_lst = []

# Accessing individual items per list
for rucksack_list in no_newline_list:
    not_found_yet = True
    for rucksack in rucksack_list:
        items_per_compartment = len(rucksack) / 2
        for item in rucksack:
            current_num += 1
            if current_num <= items_per_compartment:
                first_compartment.append(item)
            else:
                second_compartment.append(item)
    # print(f'First: {first_compartment}')
    # print(f'Second: {second_compartment}')
    # print()
    for item in first_compartment:
        if (item in second_compartment) and (not_found_yet == True):
            # print(f"\tAdding {item} to duplicates\n")
            duplicates.append(item)
            not_found_yet = False

    #print(duplicates)
    #print()
    current_num = 0
    first_compartment = []
    second_compartment = []

# print(duplicates)

sum_priorities = 0
for item in duplicates:
    sum_priorities += priorities[item]

print(sum_priorities) # Answer: 8233'''
