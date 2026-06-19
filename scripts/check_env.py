# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# # 1. 加载 .env 文件中的密钥
# load_dotenv()

# # 2. 从环境变量中读取 DeepSeek Key
# api_key = os.getenv("DEEPSEEK_API_KEY")

# # 3. 检查是否读取成功
# print("=" * 30)
# if api_key:
#     print("✅ 密钥读取成功！(前6位: " + api_key[:6] + "...)")
# else:
#     print("❌ 密钥读取失败！请检查 .env 文件是否在项目根目录，且内容为 DEEPSEEK_API_KEY=sk-xxx")
#     exit()

# # 4. 初始化 DeepSeek 客户端（注意 base_url 必须指向 deepseek）
# client = OpenAI(
#     api_key=api_key,
#     base_url="https://api.deepseek.com"
# )

# # 5. 尝试发送一条最简单的消息
# try:
#     print("🔄 正在连接 DeepSeek API，请稍候...")
#     response = client.chat.completions.create(
#         model="deepseek-chat",
#         messages=[
#             {"role": "user", "content": "请只回复：你好"}
#         ],
#         max_tokens=10  # 设置短一点，省点钱
#     )
    
#     # 6. 打印返回的结果
#     result = response.choices[0].message.content
#     print("🤖 模型返回结果: " + result)
#     print("✅ 恭喜！环境彻底配置成功！可以开始 Day 2 了。")
    
# except Exception as e:
#     print("❌ 调用失败，报错信息如下：")
#     print(e)
# print("=" * 30)

import os
from dotenv import load_dotenv
import dashscope
from dashscope import Generation

# 1. 加载 .env 文件中的密钥
load_dotenv()

# 2. 从环境变量中读取 DashScope API Key
api_key = os.getenv("DASHSCOPE_API_KEY")

# 3. 检查是否读取成功
print("=" * 30)
if api_key:
    print("✅ 密钥读取成功！(前6位: " + api_key[:6] + "...)")
else:
    print("❌ 密钥读取失败！请检查 .env 文件")
    exit()

# 4. 设置 API Key
dashscope.api_key = api_key

# 5. 尝试发送一条最简单的消息
try:
    print("🔄 正在连接千问 API，请稍候...")
    response = Generation.call(
        model='qwen-turbo',  # 也可以尝试 qwen-plus 或 qwen-max[reference:16]
        messages=[{'role': 'user', 'content': '你好吗'}],
        result_format='message'  # 设置为 'message' 以获取结构化返回
    )
    
    # 6. 打印返回的结果
    if response.status_code == 200:
        result = response.output.choices[0].message.content
        print("🤖 模型返回结果: " + result)
        print("✅ 恭喜！环境彻底配置成功！可以开始 Day 2 了。")
    else:
        print(f"❌ 调用失败，状态码: {response.status_code}")
        print(response.message)

except Exception as e:
    print("❌ 调用失败，报错信息如下：")
    print(e)
print("=" * 30)