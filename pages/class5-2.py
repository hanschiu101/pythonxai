import openai
from dotenv import load_dotenv
import os

load_dotenv()  # 載入.env檔案內容

# 設定OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    user_input = input("你:")  # 讓使用者輸入對話內容
    if user_input.lower() in ["exit", "quit"]:
        break

    response = openai.chat.completions.create(
        model="gpt-5.1-chat-latest",
        messages=[
            {
                "role": "system",
                "content": "你是一個可以幫你回答任何關於自然語言的問題的AI助手。",
            },
            {"role": "user", "content": user_input},
        ],
    )

    assistant_message = response.choices[0].message.content
    print(f"AI:{assistant_message}")
