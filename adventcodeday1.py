final_list = []

with open('puzzle1.txt', 'r') as filename:
    lines = filename.readlines()
    num_lines = len(lines)
    current_line = 0
    elf_list = []
    for element in lines:
        current_line += 1
        if element == '\n':
            # When there is a newline character,
            # this means the current elf's information
            # has been read completely, so the
            # container used to pick up each elf's
            # information should be reset after that
            final_list.append(elf_list)
            elf_list = []
        else:
            removed_newlines = element.split('\n')
            if '' in removed_newlines:
                removed_newlines.remove('')
            converted_int = [int(i) for i in removed_newlines]
            for number in converted_int:
                elf_list.append(number)
            
final_list.append([12828, 2639, 10883, 10054, 13688])
print(final_list)

list_sums = []

for elf_list in final_list:
    list_sums.append(sum(elf_list))

max_sum_1 = max(list_sums)
print(max_sum_1)

elf_num = 1
for elf_list in final_list:
    if max_sum_1 == sum(elf_list):
        # print(f"This list: {elf_list}")
        break
    else:
        elf_num += 1

list_sums.remove(max_sum_1)
max_sum_2 = max(list_sums)
print(max_sum_2)

list_sums.remove(max_sum_2)
max_sum_3 = max(list_sums)
print(max_sum_3)

final_sum = max_sum_1 + max_sum_2 + max_sum_3
print(final_sum)
