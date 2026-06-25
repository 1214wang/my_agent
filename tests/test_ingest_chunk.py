# 测试 ingest 和 chunk 模块的完整流程
import sys
import os
# 把项目根目录加入 sys.path，确保能找到 app 包
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag.ingest import load_document
from app.rag.chunk import chunk_documents
def main():
    # 1. 加载文档
    file_path = "data/test_1.txt"
    print(f"正在加载文档：{file_path}")
    documents = load_document(file_path)
    print(f"加载完成，共 {len(documents)} 个文档单元")
    # 打印第一个文档的元数据，看看 doc_id 和页码
    if documents:
        print(f'第一个文档的元数据doc_id是:{documents[0]["doc_id"]},页码是：{documents[0]["metadata"]["page"]}')

    # 2. 切片
    print("\n开始切片...")
    chunks=chunk_documents(documents,chunk_overlap=10,chunk_size=50)
    print(f"切片完成，共生成 {len(chunks)} 个切片")
    # 打印前 3 个切片的内容和 chunk_id
    for i, chunk in enumerate(chunks[:3]):
        print(f"\n--- 切片 {i+1} ---")
        print(f"chunk_id: {chunk['chunk_id']}")
        print(f"内容: {chunk['text'][:30]}...")  # 只打印前30个字符，避免刷屏
        print(f"来源: {chunk['metadata']['source']}")
if __name__ == "__main__":
    main()