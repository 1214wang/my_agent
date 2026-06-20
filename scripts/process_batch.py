import os
import pandas as pd
from tqdm import tqdm
from llm_batch_enricher import analyze_review

# ============================================================
# 批量处理函数
# ============================================================
def process_batch(input_path, output_path, max_rows=None):#input_path：输入路径, output_path：输出路径
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
    df.drop('analysis', axis=1, inplace=True
    
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
if __name__ == "__main__":
    # 先只跑 3 条测试，确认没问题后再改 None
    relust=process_batch(
        input_path='./data/reviews.csv',
        output_path='./data/reviews_result.xlsx',
        max_rows=None   # 先测3条，跑通后改成 None 跑全部
    )
    print(relust)