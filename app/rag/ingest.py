# 读取 TXT/PDF/Markdown
# 为每个文档生成稳定的 doc_id（基于文件路径的 SHA256 哈希）
# 返回带元数据的文档结构
# app/rag/ingest.py
# 功能：加载本地文档，生成稳定 doc_id，附带元数据

import os
import hashlib
from typing import List, Dict, Any
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredMarkdownLoader

def compute_doc_id(source: str) -> str:
    """
    基于文件路径生成稳定的 doc_id（16位哈希）
    同一文件每次加载 doc_id 不变
    """
    return hashlib.sha256(source.encode('utf-8')).hexdigest()[:16]

def load_document(file_path: str) -> List[Dict[str, Any]]:
    """
    根据文件扩展名选择加载器，返回文档列表
    每个文档包含：doc_id, text, metadata
    """
    ext = os.path.splitext(file_path)[1].lower()
    
    # 选择合适的加载器
    if ext == ".txt":
        loader = TextLoader(file_path, encoding='utf-8')
    elif ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".md":
        loader = UnstructuredMarkdownLoader(file_path)
    else:
        raise ValueError(f"不支持的文件格式: {ext}")
    
    # 加载原始文档
    docs = loader.load()
    doc_id = compute_doc_id(file_path)
    
    result = []
    for i, doc in enumerate(docs):
        result.append({
            "doc_id": doc_id,
            "text": doc.page_content,
            "metadata": {
                "source": file_path,                  # 文件路径
                "title": os.path.basename(file_path), # 文件名
                "doc_version": str(os.path.getmtime(file_path)),  # 文件修改时间（用于版本追踪）
                "source_mtime": os.path.getmtime(file_path),
                "page": doc.metadata.get("page", i + 1)  # 页码（PDF 有效）
            }
        })
    return result