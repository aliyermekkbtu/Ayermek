import re
def match_anything_ending_in_b(s):
    pattern = r'a.*b$'
    return re.fullmatch(pattern, s) is not None

# Test cases
print(match_anything_ending_in_b('acb'))        # True
print(match_anything_ending_in_b('a123b'))      # True
print(match_anything_ending_in_b('a'))          # False
print(match_anything_ending_in_b('abc'))        # False
