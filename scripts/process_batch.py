import os
import pandas as pd
from tqdm import tqdm
from app.llm.client import analyze_review
import argparse

# ============================================================
# 批量处理函数
# ============================================================
#input_path：输入路径, output_path：输出路径
def process_batch(input_path, output_path, max_rows=None, temperature=0.3, top_p=0.7, frequency_penalty=1.1):
    """
    读取 CSV，对 content 列逐条调用 analyze_review，生成新列，保存结果
    """
    # 1. 读取 CSV（注意中文编码）
    df = pd.read_csv(input_path, encoding='utf-8')
    
    # 2. 如果指定了 max_rows，只取前 N 条（测试时用）
    if max_rows:
        df = df.head(max_rows)
    
    print(f" 共加载 {len(df)} 条数据，开始批量处理...")
    
    # 3. 核心：用 tqdm 包裹 apply，显示进度条
    tqdm.pandas(desc="正在分析评论")
    df['analysis'] = df['content'].progress_apply(analyze_review)
    
    # 4. 从 dict 中拆出 sentiment 和 keywords
    df['sentiment'] = df['analysis'].apply(lambda x: x.get('sentiment', '未知'))
    #join()使用方法为"分隔符".join(可迭代列表)
    df['keywords'] = df['analysis'].apply(lambda x: ', '.join(x.get('keywords', [])))
    
    # 5. 删除临时列（可选，保留也可以）
    df.drop('analysis', axis=1, inplace=True)
    
    # 6. 保存为 Excel
    df.to_excel(output_path, index=False)
    print(f"✅ 结果已保存至: {output_path}")
    
    # 7. 打印统计报告
    #value_counts专门用来做“频次统计”的方法,默认按次数从高到低排序（最多的排最前）。
    print("\n📈 情感分布统计:")
    print(df['sentiment'].value_counts())
    
    return df

# ============================================================
# 程序入口：直接运行本文件时执行
# ============================================================
# if __name__ == "__main__":
#     # 先只跑 3 条测试，确认没问题后再改 None
#     relust=process_batch(
#         input_path='./data/reviews.csv',
#         output_path='./data/reviews_result.xlsx',
#         max_rows=None   # 先测3条，跑通后改成 None 跑全部
#     )
#     print(relust)

if __name__ == "__main__":
    # 1. 创建解析器
    parser = argparse.ArgumentParser(description="AI 批量评论分析工具")
    
    # 2. 定义五个参数
    parser.add_argument('-i', '--input', default='data/reviews.csv', help='输入 CSV 文件路径')
    parser.add_argument('-o', '--output', default='data/reviews_result.xlsx', help='输出 Excel 文件路径')
    parser.add_argument('-l', '--limit', type=int, default=None, help='限制处理行数（测试用）')
    parser.add_argument('--temperature', type=float, default=0.3, help='温度参数')
    parser.add_argument('--top_p', type=float, default=0.7, help='核采样参数')
    parser.add_argument('--frequency_penalty', type=float, default=1.1, help='重复惩罚参数')
    
    # 3. 解析终端输入
    args = parser.parse_args()
    
    # 4. 调用核心函数
    process_batch(args.input, args.output, args.limit,temperature=args.temperature,top_p=args.top_p,frequency_penalty=args.frequency_penalty) 