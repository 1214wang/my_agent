from app.llm.client import analyze_review

# ============================================================
# 测试区
# ============================================================
if __name__== "__main__":
    test_texts = [
        "产品质量太差了，用了三天就坏了",
        "客服态度特别好，解决问题很快",
        "物流速度一般，但东西还不错"
    ]
    for i in test_texts:
        result=analyze_review(i)
        print(f"输入: {i}")
        print(f"输出: {result}")
        print("-" * 30)