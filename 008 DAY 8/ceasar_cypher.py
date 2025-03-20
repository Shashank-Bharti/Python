import splash
print(splash.splashscreen)

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


repetition = False
while not repetition :

    direction = input("Type 'encode' to encrypt the message and 'decode' to decipher it: \n" ).lower()
    text = input("Enter your message: ").lower()
    shift = int(input("Type the shift number: \n"))

    # func create enpcrypt with text and shift
    if direction == 'encode':

        def encrypt(original_text,shift_amount):
            cipher_text = ""
            for letter in original_text :
                
                if letter not in alphabets:
                    
                    cipher_text += letter
                else:
                    shifted_pos = alphabets.index(letter) + shift_amount
                    shifted_pos %= len(alphabets)
                    cipher_text += alphabets[shifted_pos] 
                    
            print(f"Your ciphered message is '{cipher_text}'")
            
        encrypt(original_text= text , shift_amount= shift)
        user_choice = input("Do you want to restart the program type 'Yes' or 'No': \n").lower()

        if user_choice == 'no':
            repetition = True    
            print("Thanks for using Ceasar Cipher!")
                
    elif direction == 'decode':
        def decrypt(original_text,shift_amount):
            decipher_text = ""
            for letter in original_text :
                
                if letter not in alphabets:
                    decipher_text += letter
                else:
                    shifted_pos = alphabets.index(letter) - shift_amount
                    shifted_pos %= len(alphabets)
                    decipher_text += alphabets[shifted_pos] 
                
            print(f"Your deciphered message is '{decipher_text}'")
            
        decrypt(original_text= text , shift_amount= shift)
        user_choice = input("Do you want to restart the program type 'Yes' or 'No': \n").lower()

        if user_choice == 'no':
            repetition = True      
            print("Thanks for using Ceasar Cipher!")
  
    


