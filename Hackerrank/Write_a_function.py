#Write a Function
def is_leap(year):
    if year % 4 != 0 or (year % 400 != 0 and year % 100 == 0):
        leap = False
    else:
        leap = True
    
    # Write your logic here
    
    return leap

