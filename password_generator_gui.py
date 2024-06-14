import random
import string
import tkinter as tk
from tkinter import messagebox, scrolledtext
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
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
    if length < 8:
        raise ValueError("密碼長度必須至少為8")

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


def generate_and_display_password():
    try:
        length = int(length_var.get())
        if length < 8:
            messagebox.showerror("錯誤", "密碼長度必須至少為8")
            return

        use_upper = uppercase_var.get()
        use_lower = lowercase_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        password, strength = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"生成的密碼: {password}\n密碼強度: {strength}\n")
        result_text.config(state=tk.DISABLED)

        global generated_password
        generated_password = password

    except ValueError as e:
        messagebox.showerror("錯誤", str(e))


def copy_generated_password():
    if generated_password:
        pyperclip.copy(generated_password)
    else:
        messagebox.showerror("錯誤", "沒有生成的密碼可複製")


def update_length_label(val):
    length_label.config(text=f"{int(float(val))}")


def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')


# 創建主窗口
root = ttk.Window(themename="superhero")
root.title("密碼生成器")
root.resizable(True, True)

# 密碼長度
length_frame = ttk.Frame(root)
length_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

ttk.Label(length_frame, text="密碼長度:", font=("Helvetica", 12)).pack(side="left")
length_var = tk.IntVar(value=8)

minus_button = ttk.Button(length_frame, text="-", command=lambda: length_scale.set(length_var.get() - 1))
minus_button.pack(side="left", padx=5)

length_scale = ttk.Scale(length_frame, from_=8, to_=100, orient="horizontal", variable=length_var,
                         command=update_length_label, length=400)  # 設置長度為400像素
length_scale.pack(side="left")

plus_button = ttk.Button(length_frame, text="+", command=lambda: length_scale.set(length_var.get() + 1))
plus_button.pack(side="left", padx=5)

length_label = ttk.Label(length_frame, text="8")
length_label.pack(side="left", padx=5)

# 包含字符類型選項
options_frame = ttk.Frame(root)
options_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

ttk.Checkbutton(options_frame, text="包含大寫字母", variable=uppercase_var).grid(row=0, column=0, sticky="w")
ttk.Checkbutton(options_frame, text="包含小寫字母", variable=lowercase_var).grid(row=1, column=0, sticky="w")
ttk.Checkbutton(options_frame, text="包含數字", variable=digits_var).grid(row=2, column=0, sticky="w")
ttk.Checkbutton(options_frame, text="包含特殊字符", variable=symbols_var).grid(row=3, column=0, sticky="w")

# 結果區域
result_frame = ttk.Frame(root)
result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_text = scrolledtext.ScrolledText(result_frame, width=70, height=10, wrap=tk.WORD, state=tk.DISABLED)
result_text.pack()

# 按鈕
buttons_frame = ttk.Frame(root)
buttons_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

ttk.Button(buttons_frame, text="生成密碼", command=generate_and_display_password).pack(side="left", padx=10)
ttk.Button(buttons_frame, text="複製密碼", command=copy_generated_password).pack(side="left", padx=10)

# 初始化生成的密碼
generated_password = None

# 將窗口置中顯示在螢幕上
root.update_idletasks()
center_window(root)

root.mainloop()
