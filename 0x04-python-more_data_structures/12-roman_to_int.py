#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return 0
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    if len(roman_string) > 1:
        for i, v in enumerate(roman_string):
            if i == 0 or convert[roman_string[i - 1]] >= convert[v]:
                decimal += convert[v]
            else:
                decimal -= convert[v]
    else:
        decimal += convert[roman_string]
    if decimal < 0:
        decimal *= -1
    return decimal
