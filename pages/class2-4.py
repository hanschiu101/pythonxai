l1 = []
print(l1)  # 空串列

l2 = [1, 2, 3, 4, 5]
print(l2)  # 純數字串列

l3 = ["apple", "banana", "orange"]
print(l3)  # 純字串串列

l4 = [1, "apple", True, 3.14]
print(l4)  # 混合型串列

l5 = [1, 2, 3, [4, 5]]
print(l5)  # 巢狀串列

# 取得串列中的元素
print(l5[1])  # 2
print(l5[3])  # [4,5]
print(l5[3][0])  # 4

l6 = [1, 2, 3, "a", "b", "c"]
l7 = l6[::2]
print(l7)  # [1,2,b]
l8 = l6[1:4]
print(l8)  # [1,3,"a"]
l9 = l6[1:4:2]
print(l9)  # [2,"a"]
