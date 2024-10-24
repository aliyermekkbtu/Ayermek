import re
def insert_spaces_at_capitals(s):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, ' ', s)

# Test cases
print(insert_spaces_at_capitals('HelloWorldPython'))  # 'Hello World Python'
print(insert_spaces_at_capitals('PythonIsFun'))       # 'Python Is Fun'
