import re
def camel_to_snake(s):
    pattern = r'([a-z])([A-Z])'
    return re.sub(pattern, r'\1_\2', s).lower()

# Test cases
print(camel_to_snake('camelCaseString'))      # 'camel_case_string'
print(camel_to_snake('thisIsATest'))          # 'this_is_a_test'
