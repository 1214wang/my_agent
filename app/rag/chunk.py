# 用 RecursiveCharacterTextSplitter 切片
# 生成稳定的 chunk_id：{doc_id}::chunk_{index}
# 保留元数据（来源、chunk 索引、起止位置）
# app/rag/chunk.py
# 功能：将文档切块，生成稳定 chunk_id，附带元数据

from typing import List, Dict, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 导入类型提示，让调用者知道输入输出长什么样
from typing import List, Dict, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(
    documents: List[Dict[str, Any]],  # 输入：ingest.py 返回的文档列表（每个元素是一个字典）
    chunk_size: int = 300,            # 每个切片的最大长度（单位：字符数，近似 Token 数）
    chunk_overlap: int = 50           # 相邻两个切片之间重叠的字符数（保留上下文，防止切断关键句）
) -> List[Dict[str, Any]]:            # 输出：切片后的列表，每个切片也是一个字典
    """
    输入：load_document 返回的文档列表
    输出：chunk 列表，每个 chunk 包含 chunk_id, doc_id, text, metadata
    """

    # ============================================================
    # 第一步：初始化切片器（RecursiveCharacterTextSplitter）
    # ============================================================
    # 这个切片器的核心策略是：按"层级"切分。
    # 它首先尝试用最长的分隔符（如 "\n\n"）切，如果切出的块还是太长，就尝试下一个分隔符（如 "\n"），
    # 直到切成符合 chunk_size 的块为止。这能最大程度保留语义完整性（优先保留段落和句子结构）。
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,               # 300（你传进来的值）
        chunk_overlap=chunk_overlap,         # 50（你传进来的值）
        separators=[                         # 分隔符优先级列表（按长度从长到短）
            "\n\n",   # 优先级最高：保留段落之间的空行
            "\n",     # 其次：换行符
            "。",     # 中文句号
            "！",     # 感叹号
            "？",     # 问号
            "；",     # 分号
            "，",     # 逗号
            " ",      # 空格（英文词边界）
            ""        # 最后手段：如果以上都切不了，直接按字符硬切（极少数情况）
        ]
    )

    # ============================================================
    # 第二步：初始化结果容器
    # ============================================================
    all_chunks = []   # 用来存放最终所有文档切出来的所有切片

    # ============================================================
    # 第三步：遍历输入的每一个文档
    # ============================================================
    for doc in documents:
        # 取出文档的唯一 ID（用于后续追溯来源）
        doc_id = doc["doc_id"]
        
        # 用切片器把当前文档的正文（doc["text"]）切分成多个小块
        # 返回的是一个字符串列表（List[str]），每个字符串就是一个切片
        text_chunks = splitter.split_text(doc["text"])

        # ============================================================
        # 第四步：遍历当前文档切出的所有切片，生成带 ID 的标准格式
        # ============================================================
        for idx, chunk_text in enumerate(text_chunks):
            # 生成 chunk_id（全局唯一，且稳定可复现）
            # 格式：doc_id::chunk_序号
            # 例如 "a7b3c9d1::chunk_0" 表示这是该文档的第 1 个切片
            chunk_id = f"{doc_id}::chunk_{idx}"

            # 构造标准的切片字典（和 ingest.py 的输出格式保持一致）
            all_chunks.append({
                "chunk_id": chunk_id,                # 切片的全局唯一 ID
                "doc_id": doc_id,                    # 所属文档 ID
                "text": chunk_text,                  # 切片正文内容

                # ============================================================
                # 第五步：附加元数据（用于溯源和调试）
                # ============================================================
                "metadata": {
                    # 来源文件路径（从原始文档继承）
                    "source": doc["metadata"]["source"],
                    
                    # 切片在文档内的顺序（从 0 开始）
                    "chunk_index": idx,
                    
                    # 估算的字符起始位置（仅供参考，不精确）
                    # 注意：由于切片器可能因为分隔符和重叠调整长度，实际偏移量会稍有偏差
                    # 如需精准定位，后续需要额外解析
                    "start_char": idx * chunk_size,
                    
                    # 估算的字符结束位置（仅供参考）
                    "end_char": (idx + 1) * chunk_size,
                    
                    # 预留字段：章节路径（可用于按章节分层检索）
                    # 当前留空，后续可用启发式方法提取标题层级后填入
                    "heading_path": ""
                }
            })

    # ============================================================
    # 第六步：返回所有切片组成的列表
    # ============================================================
    return all_chunks