import random
import string

def my_fun(n):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(n))
    print(random_string)

    upper_count = 0
    lower_count = 0
    digit_count = 0

    for char in random_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1

    count_tuple = (upper_count,lower_count,digit_count)

    return count_tuple
    
a = my_fun(10)
print(a)