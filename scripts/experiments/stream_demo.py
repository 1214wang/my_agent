import os
from dotenv import load_dotenv
import dashscope
from dashscope import Generation


# --- 流式输出测试（打字机效果）---
print("--- 流式输出测试（打字机效果）---")

response = Generation.call(
    model='qwen-plus',
    messages=[{'role': 'user', 'content': '请用一句话描述下雨天'}],
    stream=True,
    result_format='message'
)

last_content = ""
for chunk in response:
    if chunk.output.choices:
        full_content = chunk.output.choices[0].message.content
        # 计算本次新增的部分
        new_part = full_content[len(last_content):]
        print(new_part, end='', flush=True)
        last_content = full_content

print("\n--- 结束 ---")