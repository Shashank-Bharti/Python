def format_case (f_name,l_name):
    if f_name == "" and l_name == "":
        return "Parameters weren't provided"   # early return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_case(input("enter your first name: "), input("enter your last name:")))