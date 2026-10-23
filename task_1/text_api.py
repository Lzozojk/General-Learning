from getpass import getpass
from openai import OpenAI

api_key = getpass("请输入 SiliconFlow API Key（输入时不会显示）：").strip()
model_id = input("请输入 SiliconFlow 控制台显示的 API 模型 ID：").strip()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.siliconflow.cn/v1"
)

try:
    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "user", "content": "请只回复：API连接成功"}
        ]
    )
    print("模型回复：", response.choices[0].message.content)
except Exception as error:
    print("API 调用失败：", error)