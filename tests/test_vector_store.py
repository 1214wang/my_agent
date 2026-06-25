# tests/test_vector_store.py
# 功能：测试完整的“加载 → 切片 → 入库 → 检索”流程

import sys
import os

# 将项目根目录加入 sys.path，确保能导入 app 包
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.rag.ingest import load_document
from app.rag.chunk import chunk_documents
from app.rag.index import build_vector_store
from app.rag.retrieve import retrieve

def main():
    # ==================== 1. 加载文档 ====================
    file_path = "data/test_1.txt"
    print(f"正在加载文档：{file_path}")
    documents = load_document(file_path)
    print(f"加载完成，共 {len(documents)} 个文档单元")

    # ==================== 2. 切片 ====================
    print("\n开始切片...")
    # 使用 chunk_size=50, overlap=10 便于展示效果
    chunks = chunk_documents(documents, chunk_size=50, chunk_overlap=10)
    print(f"切片完成，共生成 {len(chunks)} 个切片")

    # ==================== 3. 入库（向量化 + 存储） ====================
    print("\n开始入库（向量化 + 存入 Chroma）...")
    vectorstore = build_vector_store(chunks, persist_directory="./chroma_db")
    print("入库完成")

    # ==================== 4. 检索测试 ====================
    query = "什么是人工智能？"
    print(f"\n执行检索：query = '{query}'")
    results = retrieve(query, vectorstore, top_k=4)

    print(f"\n检索结果（Top-{len(results)}）：")
    for i, (doc, score) in enumerate(results):
        # doc.metadata 中包含了我们入库时加入的 chunk_id
        chunk_id = doc.metadata.get("chunk_id", "N/A")
        print(f"\n--- 结果 {i+1} ---")
        print(f"chunk_id: {chunk_id}")
        print(f"相似度分数（距离）：{score:.4f}（越小越相关）")
        print(f"内容预览：{doc.page_content[:60]}...")

if __name__ == "__main__":
    main()