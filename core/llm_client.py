import os
import json
from dotenv import load_dotenv
import dashscope
from dashscope import Generation
from core.prompts import SYSTEM_PROMPT
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
dashscope.api_key = api_key

def analyze_review(text):
    """
    输入：一条评论文本 (str)
    输出：dict，包含 sentiment (正面/负面/中性) 和 keywords (关键词列表)
    """
    # TODO: 
    # 1. 构造 Prompt，要求模型返回 JSON 格式：{"sentiment": "正面", "keywords": ["质量", "服务"]}
    # 2. 调用 Generation.call (参考 check_env.py)
    # 3. 用 json.loads() 解析返回结果
    # 4. 用 try-except 捕获 JSON 解析失败或 API 报错，异常时返回默认值 {"sentiment": "未知", "keywords": []}
    try:
        message=[{
        "role":"system",
        "content":SYSTEM_PROMPT},
        {"role":"user",
        "content":f"请分析{text}",}
        ]
        response=Generation.call(
            model='qwen-plus',
            messages=message,
            result_format="message",
    )
        result=response.output.choices[0].message.content
        # print(f"🔍 完整响应对象: {response}")          # 打印整个 response
        # print(f"🔍 状态码: {response.status_code}")    # 打印状态码
        # print(f"初始返回内容为{result}")
        result_dict=json.loads(result)
        return result_dict
    except json.JSONDecodeError as e:
        print(f"json解析失败，原因：{e}")
        return {"sentiment": "未知", "keywords": []}
    except Exception as e:
        print(f"❌ API调用失败: {e}")
        return {"sentiment": "未知", "keywords": []}