"""Leetcode solution to covert Roman numbers to their integer equivalents. Danielle, November 2019."""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Record the total value of the input roman numberal
        value_roman = 0

        # The transformations will be recorded as entries in a dict
        roman_to_int = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
            "M": 1000
        }

        len_roman = len(s)

        # Now determine if one of the keys in the dict above is equivalent to each                  part of the input string
        for i in reversed(range(len_roman)):
            for key in roman_to_int:
                if s[i] == key:
                    if i == len_roman - 1:
                        value_roman += roman_to_int.get(key)
                        previous = value_roman
                    else:
                        if roman_to_int.get(key) >= previous:
                            value_roman += roman_to_int.get(key)
                        elif roman_to_int.get(key) < previous:
                            value_roman -= roman_to_int.get(key)
                    previous = roman_to_int.get(key)

        # Now return the full value of the Roman numeral
        return value_roman