import streamlit as st

st.title("課堂筆記")
with st.expander("class1"):
    st.write(
        '''
## 🧠 一、什麼是「註解」？

👉 **註解是給人看的，電腦不會執行**

```python
# 這是單行註解
"""
這是多行註解
"""
```

就像在程式裡寫小筆記 📒

---

## 📦 二、資料的種類（變數）

就像不同形狀的盒子，裝不同東西

| 種類        | 例子             | 說明        |
| --------- | -------------- | --------- |
| 整數 int    | `3`            | 沒有小數點的數字  |
| 浮點數 float | `3.14`         | 有小數點      |
| 布林值 bool  | `True / False` | 只有「對 / 錯」 |
| 字串 str    | `"hello"`      | 文字，要加引號   |

```python
n1 = 3
n2 = 3.14
b1 = True
s1 = "hello"
```

---

## 🖨️ 三、print：把東西顯示出來

```python
print(3)
print("hello")
```

👉 就是「叫電腦說出來」

---

## ➕ 四、數學運算

```python
a = 10
b = 20
```

| 運算   | 寫法       | 說明   |
| ---- | -------- | ---- |
| 加    | `a + b`  | 加法   |
| 減    | `a - b`  | 減法   |
| 乘    | `a * b`  | 乘法   |
| 除    | `a / b`  | 除法   |
| 整數除法 | `a // b` | 不要小數 |
| 取餘數  | `a % b`  | 剩多少  |
| 次方   | `a ** 2` | 平方   |

---

## 🔤 五、字串（文字）玩法

```python
"hello" + "world"   # 合在一起
"hello" * 3         # 重複
```

結果👇
➡ `"helloworld"`
➡ `"hellohellohello"`

---

## ✨ 六、f-string（聰明的字串）

可以把變數放進文字裡！

```python
name = "alice"
age = 25
print(f"我叫{name}，今年{age}歲")
```

---

## 📏 七、len：算長度

```python
len("hello")  # 5
len("")       # 0
```

👉 看「有幾個字」

---

## 🧪 八、type：看資料是什麼種類

```python
type(10)       # int
type(3.14)     # float
type("hello")  # str
```

---

## 🔄 九、資料轉換（變魔法）

```python
int("123")    # 123
float(10)     # 10.0
str(123)      # "123"
bool(0)       # False
bool(1)       # True
```

記住小口訣 🧠

* **0、空的 → False**
* **其他 → True**

---

## ⌨️ 十、input：請使用者輸入

```python
in1 = input("請輸入內容:")
```

⚠️ input 進來的 **一定是文字（str）**

如果要算數學，要轉成 int 👇

```python
in2 = int(input("請輸入整數:"))
print(in2 * 10)
```

---

## 📐 十一、算圓面積

```python
r = int(input("請輸入半徑:"))
area = 3.14 * r**2
print(f"圓面積是 {area}")
```

---

## 🤔 十二、比較（對或錯）

```python
1 == 1   # True
1 != 1   # False
2 > 1    # True
```

---

## 🧩 十三、邏輯運算

* `not`：相反
* `and`：而且（都要對）
* `or`：或（有一個對就好）

```python
True and False  # False
True or False   # True
```

---

## 🚪 十四、if 判斷（做選擇）

```python
password = input("請輸入密碼:")
if password == "1234":
    print("登入成功")
else:
    print("密碼錯誤")
```

👉 就像：

* 如果對 → 做這件事
* 不然 → 做另一件事

---

## 🌐 十五、Streamlit（做網頁）

```python
import streamlit as st
st.title("這是首頁")
```

👉 可以做簡單的網頁畫面！

---

### 🎉 小總結

今天你學會了：
✅ 變數
✅ 數學
✅ 文字
✅ 使用者輸入
✅ 判斷對錯
✅ 做選擇（if）



'''
    )
