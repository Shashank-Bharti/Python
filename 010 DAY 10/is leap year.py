def is_leap_year(year):
    # Write your code here. 
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is a leap year."
            else:
                return f"{year} is not a leap year."
        else:
            return f"{year} is a leap year."
    else:
        return f"{year} is not a leap year."
            
    # Don't change the function name.
    
print(is_leap_year(2100))