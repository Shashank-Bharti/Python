try :
    age = int(input("How old are You? "))
except ValueError:
    print("You've entered an invalid answer.\nTry answering in numerical values (example: 15)")
    age = int(input("How old are You? "))
if age >= 18 :
    print(f"You can Apply for Driving License {age}")
1