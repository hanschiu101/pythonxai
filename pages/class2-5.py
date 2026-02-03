print(len([]))  # 0
print(len(["蘋果"]))  # 1
print(len([1, 2, 3, 4, 5]))  # 5
print(len([1, 2, 3, [4, 5]]))  # 4
print(len([1, 2, 3, [4, 5], 6]))  # 6
print(len([1, 2, 3, [4, 5], 6, 7]))  # 7
print(len([1, 2, 3, [4, 5], 6, 7, 8]))  # 8
print(len([1, 2, 3, [4, 5], 6, 7, 8, 9]))  # 9
print(len([1, 2, 3, [4, 5], 6, 7, 8, 9, 10]))  # 10
print(len([1, 2, 3, [4, 5], 6, 7, 8, 9, 10, 11]))  # 11
print(len([1, 2, 3, [4, 5], 6, 7, 8, 9, 10, 11, 12]))  # 12
print(len([1, 2, 3, [4, 5], 6, 7, 8, 9, 10, 11, 12, 13]))  # 13

l1 = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
# 遍歷串列1
for i in range(len(l1)):
    print(l1[i])
# 遍歷串列2
for element in l1:
    print(element)

print("-" * 30)
a = [1, 2, 3]
a[0] = 10
print(a)  # [10,2,3]

print("-" * 30)
a = [1, 2, 3]
b = a
b[0] = 10
print(a)  # [10,2,3]
print(b)  # [10,2,3]

print("-" * 30)
l2 = [1, 2, 3]
l2.append(4)
print(l2)  # [1,2,3,4]

l3 = [1, 2, 3, 1]
l3.remove(1)
print(l3)  # [2,3,1]
l3.remove(1)
print(l3)  # [2,3]

l4 = [
    1,
    2,
    3,
]
l4.pop()
print(l4)  # [1,2,]
l4.pop(0)
print(l4)  # [2]

l5 = [3, 4, 1, 5, 2]
l5.sort()
print(l5)  # [1,2,3,4,5]
