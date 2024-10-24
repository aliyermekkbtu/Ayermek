import re
def find_upper_followed_by_lower(s):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, s)

# Test cases
print(find_upper_followed_by_lower('Hello World'))    # ['Hello', 'World']
print(find_upper_followed_by_lower('PythonisFun'))    # ['Python']
print(find_upper_followed_by_lower('PYTHON'))         # []

