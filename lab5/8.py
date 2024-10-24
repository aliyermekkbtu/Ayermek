import re
def split_at_uppercase(s):
    pattern = r'[A-Z][^A-Z]*'
    return re.findall(pattern, s)

# Test cases
print(split_at_uppercase('HelloWorldPython'))  # ['Hello', 'World', 'Python']
print(split_at_uppercase('PythonIsFun'))       # ['Python', 'Is', 'Fun']
