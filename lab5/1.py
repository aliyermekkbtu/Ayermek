import re

def match_zero_or_more_b(s):
    pattern = r'ab*'
    return re.fullmatch(pattern, s) is not None

# Test cases
print(match_zero_or_more_b('a'))        
print(match_zero_or_more_b('ab'))       
print(match_zero_or_more_b('abb'))      
print(match_zero_or_more_b('b'))        