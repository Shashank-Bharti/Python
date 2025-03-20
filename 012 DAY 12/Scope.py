'''
Global scope:
'''
enemies = 1

def level():
    if enemies > 0 :
        print("Easy")
        
    elif enemies > 2 :
        print("medium")
        
print (enemies)
level()


'''
Local scope:
'''
health = 0

def potion():
    
    healing_potion = 2
    
    return healing_potion
    
# print(healing_potion) <---- Cant be called here as it is locally defined in potion()

# Python doesnt have a block scope 
