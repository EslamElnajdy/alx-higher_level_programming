#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) != str:
        return 0
    roman_di = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in roman_string:
        if roman_di[i] > num:
            num = roman_di[i] - num
        else:
            num += roman_di[i]
    return num
