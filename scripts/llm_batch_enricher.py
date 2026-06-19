import os
import json
from dotenv import load_dotenv
import dashscope
from dashscope import Generation
# 1. 加载环境变量
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
dashscope.api_key = api_key

# ============================================================
# 任务 A：封装单条文本的处理函数（你需要自己写！）
# ============================================================
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
        "content":"你现在是一名文本分析专家，请对用户评论输出JSON，"
        "回答格式为{\"sentiment\":\"正面\负面\中立\",\"keywords\":[\"关键词1\",\"关键词2\"]},直接输出JSON，不要有其他废话"},
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
# ============================================================
# 任务 B：批量处理主流程（你要把 pandas 应用写出来）
# ============================================================
# def process_batch(input_path, output_path, max_rows=None):
#     """
#     读取 CSV，对 content 列逐条调用 analyze_review，生成新列，保存结果
#     """
#     # 1. 用 pd.read_csv 读取文件
#     df = pd.read_csv(input_path)
    
#     # 2. 如果 max_rows 有值，只取前 N 条（测试时用，省 token 和省钱）
#     if max_rows:
#         df = df.head(max_rows)
    
#     print(f"📊 共加载 {len(df)} 条数据，开始批量处理...")
    
#     # 3. TODO: 用 df.apply() 或迭代，为每条数据调用 analyze_review
#     #    提示：使用 df['content'].apply(analyze_review) 会返回一列 dict
#     #    然后用 pd.json_normalize 或直接拆成两列（sentiment 和 keywords）
    
#     # 4. TODO: 将结果合并回原 df，新增 'sentiment' 和 'keywords' 列
    
#     # 5. TODO: 保存为 Excel 或 CSV（用 df.to_excel 或 df.to_csv）
    
#     # 6. TODO: 打印一个简单的统计报告（各类情感的数量占比）
    
#     return df


# ============================================================
# 测试区
# ============================================================
if __name__== "__main__":
    test_texts = [
        "产品质量太差了，用了三天就坏了",
        "客服态度特别好，解决问题很快",
        "物流速度一般，但东西还不错"
    ]
    for i in test_texts:
        result=analyze_review(i)
        print(f"输入: {i}")
        print(f"输出: {result}")
        print("-" * 30)