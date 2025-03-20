import random

# random_number = random.randint(1,10)
# print(random_number)

# rand_float_0_10 = random.random()
# print(rand_float_0_10)


# rand_float_0_10 = random.random()*5
# print(rand_float_0_10)

'''logic:
random init with constraint from 1-2 , if random returns 1 then hads else prints tails 
'''
rand_num= random.randint(1,2)

if rand_num == 1 :
    print("Heads!")
    
else:
    print("Tails!")