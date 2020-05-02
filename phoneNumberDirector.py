#Find phone number from text.
def check_number(get_number):
    if len(get_number) == 11:
        for i in range(0, 11):
            if not get_number[i].isdecimal():
                return False
        if get_number[0] != '0' and get_number[1] != '1':
            return False
    else:
        for i in range(1, 14):
            if not get_number[i].isdecimal():
                return False
        if get_number[0] != '+' and get_number[1] != '8':
            return False

    return True


message = "This is Sonjoy Pall my contact numbers are +8801765255101 or 01732368626 or +8801758252635 You can cantact within 12am - 8 am"
found_number = False

for i in range(len(message)):
    if i <= len(message) - 14:
        case_1 = message[i:i+11]
        case_2 = message[i:i+14]

        if check_number(case_2):
            real_value = case_2
            print("Phone number is found: " + case_2)
            found_number = True

        if check_number(case_1):
            if case_1 in real_value:
                continue
            print("Phone number is found: " + case_1)
            found_number = True

if not found_number:
    print("Could not find any phone number")
