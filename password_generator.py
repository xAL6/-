#!/usr/bin/env python3

import random
import string
import argparse
import pyperclip

def check_strength(password):
    length_criteria = len(password) >= 12
    digit_criteria = any(char.isdigit() for char in password)
    upper_criteria = any(char.isupper() for char in password)
    lower_criteria = any(char.islower() for char in password)
    symbol_criteria = any(char in string.punctuation for char in password)

    strength = sum([length_criteria, digit_criteria, upper_criteria, lower_criteria, symbol_criteria])

    if strength == 5:
        return "強"
    elif strength >= 3:
        return "中"
    else:
        return "弱"

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    if length < 8 or length > 100:
        raise ValueError("密碼長度必須介於8到100之間")

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("至少必須選擇一種字符集")

    # 確保密碼包含至少一個每種選擇的字符集的字符
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # 用隨機選擇的字符填充剩餘的密碼長度
    while len(password) < length:
        password.append(random.choice(characters))

    # 打亂順序避免可預測的序列
    random.shuffle(password)
    password = ''.join(password)

    strength = check_strength(password)
    return password, strength

def main():
    help_text = """
    密碼生成器腳本

    範例：
      生成默認長度為10的密碼，包含大寫字母、小寫字母和數字：
        python password_generator.py

      生成長度為12的密碼，包含所有字符集：
        python password_generator.py -l 12 -a

      生成長度為8的密碼，只包含數字和小寫字母：
        python password_generator.py -l 8 -d -L

      生成一個密碼並複製到剪貼板：
        python password_generator.py -l 12 -a -c
    """

    parser = argparse.ArgumentParser(description="密碼生成器\n" + help_text, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-l', '--length', type=int, default=10, help="密碼長度（默認值：10）")
    parser.add_argument('-a', '--all', action='store_true', help="包含大寫字母、小寫字母、數字和特殊字符")
    parser.add_argument('-u', '--uppercase', action='store_true', help="包含大寫字母")
    parser.add_argument('-L', '--lowercase', action='store_true', help="包含小寫字母")
    parser.add_argument('-d', '--digits', action='store_true', help="包含數字")
    parser.add_argument('-s', '--symbols', action='store_true', help="包含特殊字符")
    parser.add_argument('-c', '--copy', action='store_true', help="複製到剪貼板")

    args = parser.parse_args()

    if args.length < 8 or args.length > 100:
        parser.error("密碼長度必須介於8到100之間")

    # 如果指定了 -a 參數，設置所有字符集為 True
    if args.all:
        args.uppercase = True
        args.lowercase = True
        args.digits = True
        args.symbols = True

    # 如果沒有指定任何字符集，設置默認字符集
    if not (args.uppercase or args.lowercase or args.digits or args.symbols):
        args.uppercase = True
        args.lowercase = True
        args.digits = True

    try:
        password, strength = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.symbols)
        print(f"生成的密碼: {password}")
        print(f"密碼強度: {strength}")

        if args.copy:
            pyperclip.copy(password)
            print("密碼已複製到剪貼板")

        # 添加顏文字
        print("( ͡° ͜ʖ ͡°) 密碼生成成功！")

    except ValueError as e:
        print(f"錯誤: {e}")

if __name__ == "__main__":
    main()
