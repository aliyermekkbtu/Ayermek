import re
def match_two_to_three_b(s):
    pattern = r'ab{2,3}'
    return re.fullmatch(pattern, s) is not None

# Test cases
print(match_two_to_three_b('ab'))       # False
print(match_two_to_three_b('abb'))      # True
print(match_two_to_three_b('abbb'))     # True
print(match_two_to_three_b('abbbb'))    # False

