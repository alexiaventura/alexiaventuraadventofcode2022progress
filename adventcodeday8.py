with open('puzzle8.txt', 'r') as filename:
    lines = filename.readlines()

# print(lines)

no_newline_list = []

for element in lines:
    removed_newlines = element.split('\n')
    if '' in removed_newlines:
        removed_newlines.remove('')
    no_newline_list.append(removed_newlines)

# print(no_newline_list)

no_brackets = []

for lst in no_newline_list:
    for element in lst:
        no_brackets.append(element)

# print(no_brackets)

converted_int = []

for element in no_brackets:
    converted_int.append(int(element))

# print(converted_int)

num_trees = 0

# Outer trees are added up (top and bottom rows)
for row_trees in converted_int:
    if converted_int[0] == row_trees:
        num_trees += len(str(row_trees))
    if converted_int[-1] == row_trees:
        num_trees += len(str(row_trees))

# Left and right sides of block of trees
for row_tree in converted_int:
    first_found = False
    last_found = False
    for tree in str(row_tree):
        if (str(row_tree)[0] == tree) and (first_found == False):
            num_trees += 1
            first_found = True
        if (str(row_tree)[-1] == tree) and (last_found == False):
            num_trees += 1
            last_found = True

# Total number of trees making the perimeter should be 396

left_trees = ['L'] # trees in previous index positions
right_trees = ['R'] # trees in upcoming index positions
up_trees = ['U'] # trees in the same index positions in previous lists
bottom_trees = ['B'] # trees in same index positions in future lists

tree_dct = {}
big_tree_lst = []
tree_lst = []

# 1234567

current_row = 0
# Finding inner trees that are visible
for row_tree in converted_int:
    if (row_tree != converted_int[0]) and (row_tree != converted_int[-1]):
        # Excludes top and bottom rows of trees
        for pos in range(len(str(row_tree))):
            # Excludes trees on left and right edges
            # if (str(row_tree)[0] != str(row_tree)[pos]) and (str(row_tree)[-1] != str(row_tree)[pos]):
            if (pos != 0) or (pos != len(str(row_tree)) - 1):
                # Doing trees on the right first
                # if str(row_tree)[len(row_tree) - pos] < len(row_tree):
                # Staying within the range (position + x = length of row --> x = len - pos)
                right_trees.append(str(row_tree)[pos + 1:(len(str(row_tree)))])
                left_trees.append(str(row_tree)[0:pos])
            # tree_dct["Row " + str(current_row) + ": " + str(row_tree)[pos]] = right_trees
            tree_lst.append(str(current_row))
            tree_lst.append(int(str(row_tree)[pos]))
            # tree_lst.append(int(str(row_tree)[pos - 2]))
            tree_lst.append(right_trees)
            tree_lst.append(left_trees)
            big_tree_lst.append(tree_lst)
            right_trees = ['R']
            left_trees = ['L']
            tree_lst = []
    current_row += 1

# Testing for correct right trees:
'''for lst in big_tree_lst:
    if lst[0] == '1' or lst[0] == '2':
        print(lst)'''

for lst in big_tree_lst[:]:
    if '' in lst[2] or '' in lst[3]:
        big_tree_lst.remove(lst)


for lst in big_tree_lst:
    if lst[0] == '1' or lst[0] == '2':
        print(lst)



# print(num_trees)
