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
        result = 0
        int_numerals = self.int_letters(roman_string)
        for i, num in enumerate(int_numerals):
            if i+1 == len(int_numerals) or num >= int_numerals[i+1]:
                result += num
            else:
                result -= num
        return result

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
    result = converter.romanToInt(roman_string=roman)

    print(result)
