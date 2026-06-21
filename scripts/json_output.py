#==============结构化输出====================
#让模型必须返回 JSON，并成功用 json.loads() 解析出字段。
import json
from core.llm_client import generate_response
from core.prompts import EXTRACTION_PROMPT
#输出结构化内容
def get_structured_response(user_input):
    messages = [
        {"role": "system", "content": EXTRACTION_PROMPT},
        {"role": "user", "content": user_input}
    ]
    
    try:
        content = generate_response(messages, temperature=0.2)
        print(f"模型返回: {content}")
        data = json.loads(content)
        print(f"人名: {data.get('name')}, 情绪: {data.get('emotion')}")
    except Exception as e:
        print(f"处理失败: {e}")

if __name__ == "__main__":
    get_structured_response("小明今天看起来很高兴。")
    get_structured_response("李华今天要被气死了")
    get_structured_response("今天要吃啥？")
