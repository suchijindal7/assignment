import re

def is_valid_number(number: str):
    if re.match("\\d{10}", number): # for having 10 digit
        return True
    elif re.match("\\d{3}[-\\.\\s]\\d{3}[-\\.\\s]\\d{4}", number): # having digits, -, . or spaces 
        return True
    elif re.match("\\d{4}[-\\.\\s]\\d{3}[-\\.\\s]\\d{3}", number):
        return True
    elif re.match("\\d{3}-\\d{3}-\\d{4}\\s(x|(ext))\\d{3,5}", number): # having digits and extension (length 3 to 5)  
        return True
    elif re.match("\\(\\d{3}\\)-\\d{3}-\\d{4}", number): #  having digits and area code in braces  
        return True
    elif re.match("\\(\\d{3}\\)\\d{3}-\\d{4}", number): #  having digits and area code in braces  
        return True
    elif re.match("\\(\\d{5}\\)-\\d{3}-\\d{3}", number):
        return True
    elif re.match("\\(\\d{4}\\)-\\d{3}-\\d{3}", number):
        return True
    elif re.match("\\+\\d{10}", number):
        return True
    elif re.match("\\d{1}-\\d{3}-\\d{3}-\\d{4}", number):
        return True
    elif re.match("\\+\\d{3}-\\d{3}-\\d{4}", number):
        return True
    else:
        return False
    
    
phone_list = [
    '2124567890',
    '212-456-7890',
    '(212)456-7890',
    '(212)-456-7890',
    '212.456.7890',
    '212 456 7890',
    '+12124567890',
    '+12124567890',
    '+1 212.456.7890',
    '+212-456-7890',
    '1-212-456-7890'
]


for number in phone_list:
    if is_valid_number(number):
        print(f"Valid phone number: {number}")
    else:
        print("invalid")
