import pytest
import pandas as pd
from scripts.process_batch import process_batch

def test_process_batch_normal():
    # TODO 1: 用 max_rows=2 调用 process_batch，断言返回的 DataFrame 长度 == 2
    result = process_batch(
        input_path="data/reviews.csv",      # 用你实际存在的测试数据
        output_path="data/test_output.xlsx",
        max_rows=2,
        temperature=0.7,
        top_p=0.9,
        frequency_penalty=0.0
    )
    assert len(result) == 2
def test_process_batch_file_not_found():
    # TODO 2: 传入不存在的 input_path，断言抛出 FileNotFoundError
    with pytest.raises(FileNotFoundError):
        process_batch(
            input_path="data1.csv",
            output_path="output.xlsx",
            max_rows=None
        )