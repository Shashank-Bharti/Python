#TODO: Create a letter using starting_letter.txt 
with open(r"024 DAY 24\Mail Merge Project Start\Input\Letters\starting_letter.txt","r") as template:
    message = template.read()
 #for each name in invited_names.txt
 
with open (r"024 DAY 24\Mail Merge Project Start\Input\Names\invited_names.txt", "r") as invited_names:
    names = invited_names.readlines()
    
    for name in names:
        stripped_name = name.strip()
        #Replace the [name] placeholder with the actual name.
        new_letter = message.replace('[name]',stripped_name)
        #Save the letters in the folder "ReadyToSend".
        with open(f"024 DAY 24/Mail Merge Project Start/Output/ReadyToSend/Invite_for_{stripped_name}.txt",mode = "w") as custom_letter:
            custom_letter.write(new_letter)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp