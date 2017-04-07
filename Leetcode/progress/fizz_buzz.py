'''
https://leetcode.com/problems/fizz-buzz/#/description

Problem:
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output ��Fizz�� instead of the number and for the multiples of five output ��Buzz��. For numbers which are multiples of both three and five output ��FizzBuzz��.
    
Example:
n = 15,



Return:

[

    "1",

    "2",

    "Fizz",

    "4",

    "Buzz",

    "Fizz",

    "7",

    "8",

    "Fizz",

    "Buzz",

    "11",

    "Fizz",

    "13",

    "14",

    "FizzBuzz"

]

:author: babykick
:date: 2017-04-07
'''


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        data = range(1, n + 1)
        return list(map(self.convert, data))
            
    def convert(self, n):
        if n % 3 == 0 and n % 5 == 0:
            return 'FizzBuzz'
        elif n % 3 == 0:
            return 'Fizz'
        elif n % 5 == 0:
            return 'Buzz'
        return str(n)
        
            


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (15, [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz"
            ]),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().fizzBuzz(inp) == outp)
    
