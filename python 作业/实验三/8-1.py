import random
import string

def my_fun(n):
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for i in range(n))
    print(random_string)

    upper_count = 0
    lower_count = 0

    for char in random_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    text_to_write = f"大写字母出现: {upper_count} 次, 小写字母出现: {lower_count} 次\n"

    with open("english.txt", "w", encoding="utf-8") as file:
        file.write(random_string)
        file.write("\n"+text_to_write)
        
    print("字符串已写入 english.txt 文件")

my_fun(20)