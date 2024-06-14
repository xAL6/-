# 密碼生成器

這是一個用於生成強密碼的 Python 腳本。你可以選擇不同的字符集，包括大寫字母、小寫字母、數字和特殊字符來生成密碼。該腳本還可以評估密碼的強度，並提供一個 GUI 版本以便更方便地使用。

## 特性

- 自定義密碼長度
- 包含或排除大寫字母、小寫字母、數字和特殊字符
- 密碼強度評估
- 將生成的密碼複製到剪貼板
- GUI 版本可用

## 要求

- Python 3

## 安裝

首先，克隆這個倉庫到你的本地機器：

```bash
git clone https://github.com/你的用戶名/password_generator.git
```

進入倉庫目錄：

```bash
cd password_generator
```

安裝所需的 Python 包：

```bash
pip3 install -r requirements.txt
```

## 使用方法

### 命令行界面 (CLI)

運行 `password_generator.py` 來生成密碼：

```bash
python password_generator.py
```

你可以使用以下參數來自定義密碼：

- `-l`, `--length`：密碼長度（默認值：10）
- `-a`, `--all`：包含大寫字母、小寫字母、數字和特殊字符
- `-u`, `--uppercase`：包含大寫字母
- `-L`, `--lowercase`：包含小寫字母
- `-d`, `--digits`：包含數字
- `-s`, `--symbols`：包含特殊字符
- `-c`, `--copy`：複製到剪貼板
- `-h`, `--help`：顯示幫助信息

範例：

```bash
# 生成長度為12的密碼，包含所有字符集
python password_generator.py -l 12 -a

# 生成長度為8的密碼，只包含數字和小寫字母
python password_generator.py -l 8 -d -L

# 生成一個密碼並複製到剪貼板
python password_generator.py -l 12 -a -c

# 顯示幫助信息
python password_generator.py -h
```

### 圖形用戶界面 (GUI)

運行 `password_generator_gui.py` 來打開圖形用戶界面：

```bash
python password_generator_gui.py
```

在 GUI 中，你可以使用滑塊和複選框來自定義密碼選項，並生成密碼。
