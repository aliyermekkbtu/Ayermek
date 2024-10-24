import re
def snake_to_camel(s):
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Test cases
print(snake_to_camel('snake_case_string'))    # 'snakeCaseString'
print(snake_to_camel('this_is_a_test'))       # 'thisIsATest'
