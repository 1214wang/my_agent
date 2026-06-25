import os
import json
from dotenv import load_dotenv
import dashscope
from dashscope import Generation
from .prompts import EMOTION_PROMPT  

load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
dashscope.api_key = api_key


def analyze_review(text, top_p=0.7,frequency_penalty=1.1,temperature=0.7, stream=False):
    """
    输入：一条评论文本 (str)
    输出：dict，包含 sentiment 和 keywords
    """
    try:
        messages = [
            {"role": "system", "content": EMOTION_PROMPT},
            {"role": "user", "content": f"请分析：{text}"}
        ]
        response = Generation.call(
            model='qwen-plus',
            messages=messages,
            frequency_penalty=frequency_penalty,
            temperature=temperature, 
            top_p=top_p,
            stream=stream,
            result_format='message',
        )
        content = response.output.choices[0].message.content
        result_dict = json.loads(content)
        return result_dict
    except json.JSONDecodeError as e:
        print(f"json解析失败，原因：{e}")
        return {"sentiment": "未知", "keywords": []}
    except Exception as e:
        print(f"❌ API调用失败: {e}")
        return {"sentiment": "未知", "keywords": []}


def generate_response(messages, top_p=0.7,frequency_penalty=1.1,temperature=0.7, stream=False):
    """
    通用调用函数：接收 messages 列表（可包含 system/user/assistant），
    - temperature: 控制随机性
    - top_p: 核采样阈值（0~1）
    - frequency_penalty: 重复词惩罚（-2.0~2.0）
    返回模型回复的字符串，失败时抛出异常。
    """
    response = Generation.call(          
        model='qwen-plus',
        messages=messages,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        temperature=temperature,          
        result_format='message',
        stream=stream,
    )
    if stream:
        # 流式模式：直接返回生成器，让调用者迭代
        return response 
    else:
        if response.status_code == 200:
            return response.output.choices[0].message.content
        else:
            raise Exception(f"API调用失败: {response.message}")


def test_temperature(prompt, temp_value=0.7):
    """
    便捷测试函数：只传一个 prompt 字符串，打印不同温度下的回复。
    内部调用 generate_response，不重复写 API 调用逻辑。
    """
    print(f"\n--- 正在测试 Temperature = {temp_value} ---")
    messages = [{"role": "user", "content": prompt}]
    try:
        result = generate_response(messages, temperature=temp_value)  
        print(f"回复内容: {result}")
    except Exception as e:
        print(f"调用失败: {e}")