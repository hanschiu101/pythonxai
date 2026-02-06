import random


def roll_dice(n):
    results = []  # 用來存所有擲骰子的結果
    for i in range(n):
        dice = random.randint(1, 6)  # 擲一次骰子（1～6）
        results.append(dice)
    return results  # 一次回傳所有結果


# 使用者輸入擲骰子的次數
n = int(input("請輸入擲骰子的次數："))

# 呼叫函數
dice_results = roll_dice(n)

# 顯示結果
print("擲骰子的結果是：", dice_results)
