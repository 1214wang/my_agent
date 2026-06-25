import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredMarkdownLoader
import hashlib
from typing import List, Dict, Any
#定义一个能把文件加密为哈希的方法
def docs_hash(source:str)-> str:
    return hashlib.sha256(source.encode('utf-8')).hexdigest()[:16]
def load_document(file_path:str)->list[Dict[str,any]]:
    ext=os.path.splitext(file_path)[1].lower()
    if ext=='.txt':
        loader=TextLoader(file_path,encoding='etf-8')
    elif ext=='.pdf':
        loader=PyPDFLoader(file_path)
    elif ext=='.md':
        loader=UnstructuredMarkdownLoader(file_path)
    else:
        raise ValueError(f"不支持的文件格式: {ext}")
    docs=loader.load()
    doc_id=docs_hash(file_path)
    result=[]
    for i ,doc in enumerate(docs):
        result.append({
            "doc_id":doc_id,
            "text":doc.page_content,
            "metadate":{
                "source":file_path,
                "title":os.path.basename(file_path),
                "doc_version": os.path.getmtime(file_path),
                "source_mtime": os.path.getmtime(file_path),
                "page": doc.metadata.get("page",i+1),
                }
        })
    return result