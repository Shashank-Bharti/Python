#py password
#cheat to uppercase :>
# uppercase_list = [s.upper() for s in letters]
# print(uppercase_list + letters)

import random as r

print("WELCOME TO PY PASSWORD GENERATOR")

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['~','!','@','#','$','%','&','*','(',')','_','-','+','=','/',',','.',':',';']

n_letters = int(input("Enter the no. of letters you want :"))
n_numbers = int(input("Enter the no. of numbers you want :"))
n_symbols = int(input("Enter the no. of symbols you want :"))


#Easy

# password = ""

# for char in range (0 , n_letters):
#     password += r.choice(letters)
    
# for char in range (0 , n_numbers):
#     password += r.choice(numbers)
    
# for char in range (0 , n_symbols):
#     password += r.choice(symbols)

#Hard

password_list = []

for char in range (0 , n_letters):
    password_list.append(r.choice(letters))
    
for char in range (0 , n_numbers):
    password_list.append(r.choice(numbers))
    
for char in range (0 , n_symbols):
    password_list.append(r.choice(symbols))

#print(password_list)

r.shuffle(password_list)

#print(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is {password}")    
    
    


