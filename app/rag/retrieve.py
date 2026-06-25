# app/rag/retrieve.py
# 功能：根据用户问题，从向量库中检索最相似的 Top-K 切片

def retrieve(query, vectorstore, top_k=3):
    """
    检索与 query 最相似的 top_k 个切片。

    参数：
        query: str，用户问题
        vectorstore: Chroma 向量库对象
        top_k: int，返回的切片数量

    返回：
        list of (Document, score) 元组
        Document 包含 page_content 和 metadata（内含 chunk_id 等）
        score 是相似度距离（越小越相似，默认余弦距离）
    """
    # 调用 Chroma 的相似度搜索方法，返回 (Document, score) 列表
    results = vectorstore.similarity_search_with_score(query, k=top_k)
    return results