# Условия:
# 1. Длина 1 <= s.length <= 15
# 2. s состоит только из ('I', 'V', 'X', 'L', 'C', 'D', 'M')
# 3. Гарантируется, что конвертируемая в число s будет в диапозоне [1, 3999]
#
# 4. Необходимо написать решение если дан следующий python код
from typing import Dict, List

roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

class Solution:

    def __init__(self, roman_dict: Dict[str, int]):
        self.roman_dict = roman_dict
        self.roman_letters = self.roman_dict.keys()

    def romanToInt(self, roman_string: str) -> int:
        int_numerals = self.int_letters(roman_string)
        int_ = 0
        for i, num in enumerate(int_numerals):
            if i+1 == len(int_numerals) or num >= int_numerals[i+1]:
                int_ += num
            else:
                int_ -= num
        return int_

    def int_letters(self, roman_string: str) -> List[int]:
        ints = []
        for letter in roman_string:
            if letter in self.roman_letters:
                int_numeral = self.roman_dict[letter]
                ints.append(int_numeral)
            else:
                raise Exception("Wrong Roman Letter")
        return ints


if __name__ == '__main__':
    converter = Solution(roman_dict)

    roman = str(input("Enter a string - ")).upper()
    int_str = converter.romanToInt(roman_string=roman)

    print(int_str)
