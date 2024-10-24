import re
def replace_with_colon(s):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', s)

# Test cases
print(replace_with_colon('Hello, world. How are you?'))  # 'Hello:world:How:are:you?'

