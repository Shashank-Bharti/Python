splash =  """
 _    _      _                            _          _   _          
| |  | |    | |                          | |        | | | |         
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___ 
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \ 
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|
                                                                                                                                     
  _                                                                 
 | |                                                                
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __                      
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \                     
 | | | | (_| | | | | (_| | | | | | | (_| | | | |                    
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|                    
                     __/ |                                          
                    |___/                                           
   ___                                                             
 |  __ \                                                            
 | |  \/ __ _ _ __ ___   ___                                        
 | | __ / _` | '_ ` _ \ / _ \                                       
 | |_\ \ (_| | | | | | |  __/                                       
  \____/\__,_|_| |_| |_|\___| 

"""
print(splash)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''',]
words = ["apple", "cherry", "banana", "mango", "berry", "pineapple", "guava"]

 
import random as r

chosen_word = ""

chosen_word += r.choice(words)
print(chosen_word)

placeholder = ""
n_placeholder = len(chosen_word)

for letters in range(0,n_placeholder):
    placeholder += "_"
    
print(placeholder)

lives = 6

game_over = False

correct_letters = []

while not game_over :
    guess = input("Enter a letter to make your guess:").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+= letter
        else:
            display += "_"
            
            
    if guess not in chosen_word:
        lives -= 1
        
        print(f"Remaining lives {lives}")
        if lives ==0:
            game_over = True
            print("You lose")
                
            
    print(display)
    
    if "_" not in display:
        game_over = True
        print("You Win!)")
    
    print(stages[lives])