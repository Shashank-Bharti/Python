# numbers = [1, 2, 3, 4 ,5]
# new_list = []
# for n in list:
#     i = n+1
#     new_list.append(i)

# ---------------------------

# new_list = [n + 1 for n in numbers]
# print(new_list)

# ---------------------------

# name = "Shashank"
# letter_in_name = [letter for letter in name]
# print(letter_in_name)

# ---------------------------

# nums = [n**2 for n in range (1,5)]
# print(nums)

# ---------------------------

'''CONDITIONAL LIST COMP'''

names = ['Raju', 'Meera', 'Sheena', 'Hitesh', 'Rupa', 'Sahil']
selective_names = [name for name in names if len(name) > 4 ]
print(sorted(selective_names))

# ---------------------------

