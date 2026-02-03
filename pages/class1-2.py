"""
這是多行註解
"""

# 這是註解ˇ
n1 = 3  # 這是整數
n2 = 3.14  # 這是浮點數
b1 = True  # 這是布林值
s1 = "hello"  # 這是字串

print(3)
print(3.14)
print(True)
print("hello")

a = 10
b = 20
print(a + b)  # 加法
print(a - b)  # 減法
print(a * b)  # 乘法
print(a / b)  # 取整數
print(a // b)  # 取餘數
print(a % b)  # 次方

print("hello" + "wold")  # 字句串聯
print("hello" + "" + "wold")  # 字串連接
print("hello" * 3)  # 字句重複
print("hello" + "wold" * 3)  # 字句連接與重複

name = "alice"
age = 25
new_str = f"My name is {name},and I am {age} years old "  # f_string
print(new_str)

print(len(""))  # 0
print(len("hi"))  # 2
print(len("hello"))  # 5

print(type(10))
print(type(3.14))
print(type("True"))
print(type("hello"))

print(int(True))  # 1
print(int(False))  # 0
print(int("1234"))  # 1234

print(float(3.14))  # 3.14
print(float(10))  # 10.0

print(bool(1))  # True
print(bool(0))  # False
print(bool(-2))  # True
print(bool(""))  # False
print(bool("hello"))  # True

print(str(1234))  #'1234'
print(str(3.14))  #'3.14'
print(str(True))  #'True'
print(str(False))  #'False'
print(str("hello"))  #'hello'
print(str([1, 2, 3]))  #'[1, 2, 3]'
print(str({"a": 1, "b": 2}))  #'{'a': 1, 'b': 2}'
print(str((1, 2, 3)))  #'(1, 2, 3)'
print(str(None))  #'None'
print(str({"apple", "banana", "cherry"}))  # '{'banana', 'cherry', 'apple'}'
print(str(range(5)))  #'range(0, 5)'
print(str(bytes([65, 66, 67])))  # "b'ABC

in1 = input("請輸入內容")
print("你輸入的內容是:" + in1)
print(type(in1))  # str

in2 = int(input("請輸入整數:"))
print(in2 * 10)

r = int(input("請輸入半徑:"))
area = 3.14 * r**2
print(f"半徑為{r}的圓面積是{area}")

import streamlit as st

st.title("這是首頁")
