# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    cc_number = str(input())
    print('Valid' if (
        # match on any numbers starting with 4-6
        # and either have 15 consecutive numbers -> [\d]{15} or
        # have 3 consecutive numbers ([\d]{3}) and 
        # with 3 consective groups 4 numbers starting with dash (-[\d]{4}){3})
        re.match(r'^[4-6]([\d]{15}|[\d]{3}(-[\d]{4}){3})$', cc_number)
        # search for any sequences of 4 numbers, thats not allowed.
        and not re.search(r'([\d])\1\1\1', re.sub("-", "", cc_number))
     ) else 'Invalid')

