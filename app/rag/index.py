# app/rag/index.py
# 功能：将切片列表存入 Chroma 向量库，并持久化

from langchain_community.vectorstores import Chroma
from app.rag.embed import get_embedding_model

def build_vector_store(chunks, persist_directory="./chroma_db"):
    """
    接收 chunk 列表，存入 Chroma，返回 vectorstore 对象。

    参数：
        chunks: list of dict，每个 dict 必须包含 'text', 'metadata', 'chunk_id'
        persist_directory: str，持久化目录

    返回：
        Chroma 向量库对象（已持久化）
    """
    embedding_fn = get_embedding_model()

    texts = [c["text"] for c in chunks]
    ids = [c["chunk_id"] for c in chunks]

    # 确保 metadata 中包含 chunk_id，以便检索结果能溯源
    metadatas = []
    for c in chunks:
        meta = c["metadata"].copy()
        meta["chunk_id"] = c["chunk_id"]
        metadatas.append(meta)

    # 使用 LangChain 封装的 Chroma 类
    vectorstore = Chroma.from_texts(
        texts=texts,
        embedding=embedding_fn,
        metadatas=metadatas,
        ids=ids,
        persist_directory=persist_directory
    )
    vectorstore.persist()
    return vectorstore