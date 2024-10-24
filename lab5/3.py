import re
def find_lowercase_with_underscore(s):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, s)

# Test cases
print(find_lowercase_with_underscore('abc_def'))      # ['abc_def']
print(find_lowercase_with_underscore('abc_123_def'))  # ['abc_def']
print(find_lowercase_with_underscore('ABC_DEF'))      # []

