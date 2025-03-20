import random as r
import maths



def mutate(a_list):
    b_list = []
    new_item = 0
    
    for item in a_list :
        
        new_item = item * 2
        new_item += r.randint(1,3)
        new_item = new_item+item
        b_list.append(new_item)
    print(b_list) 
    
mutate([1,2,3,4,5])