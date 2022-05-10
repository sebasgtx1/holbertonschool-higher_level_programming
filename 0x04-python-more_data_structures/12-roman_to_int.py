#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    n = 0
    i = 1
    if len(roman_string) > 1:
        while (i < len(roman_string)):
            if convert[roman_string[i]] <= convert[roman_string[n]]:
                decimal += convert[roman_string[n]]
            else:
                decimal -= convert[roman_string[n]]
            n += 1
            i += 1
        decimal += convert[roman_string[n]]
    else:
        decimal += convert[roman_string]
    if decimal < 0:
        decimal *= -1
    return decimal
