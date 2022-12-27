with open('examplepuzzle7.txt', 'r') as filename:
    lines = filename.readlines()

removed_ls = []
index_pos = 0
for line in lines[:]:
    if 'ls' not in line:
        removed_ls.append(line)
        # lines.remove(lines[index_pos])
    index_pos += 1

# print(f'No ls: {removed_ls}')

removed_dollar_signs = []

for line in removed_ls:
    # print(line)
    if '$ ' in line:
        # print(f'Split line: {line.split('$ ')}')
        removed_dollar_signs.append(line.split('$ ')[1])
    else:
        removed_dollar_signs.append(line)

# print(removed_dollar_signs)

removed_newlines = []

for line in removed_dollar_signs:
    if '\n' in line:
        removed_newlines.append(line.split('\n')[0])
    else:
        removed_newlines.append(line)

# print(removed_newlines)

outer_directory = []
in_dir = None
total_sum = 0
for line in removed_newlines:
    if line == 'cd /':
        pass
    elif ('dir ' in line) and (in_dir == None):
        in_dir = False
    # elif ('dir ' in line) and (in_dir == False):
        # in_dir = True

    if ('cd ' in line) and ('cd /' not in line):
        break
    elif (in_dir == False):
        outer_directory.append(line)

# print(outer_directory)

dir_dict = {}
for element in outer_directory:
    dir_dict[element] = []

print(dir_dict)

add_here = False
mini_dir = False
saved_key = None
mini_dct = {}

while line != removed_newlines[-1]:
    for line in removed_newlines:
        print(f'Line: {line}')
        for element in dir_dict:
            if ('dir ' in element) and ('cd ' in line) and (element[4] == line[3]):
                print(f'\nKey: {element[4]}, Command: {line[3]}\n')
                add_here = element
            if ('cd ' not in line) and (add_here == element):        
                dir_dict[element].append(line)
            elif ('cd ' in line):
                for lst_ele in dir_dict[element][:]:
                    if line[3] == lst_ele[4]:
                        print(f'Line {line} and lst_ele {lst_ele} match')
                        mini_dir = True
                        saved_key = lst_ele
                        mini_dct[saved_key] = []
        if (mini_dir == True) and ('cd ' not in line) and (line not in mini_dct[saved_key]) and (saved_key not in outer_directory):
            print(f"saved key: {saved_key}")
            mini_dct[saved_key].append(line)

print(dir_dict)
print()
print(mini_dct)
