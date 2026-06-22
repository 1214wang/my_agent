from core.llm_client import generate_response
from core.prompts import CLASSIFY_PROMPT

def classify_review(text):
    #创建Few-shot 示例
    examples=[
        {"role":"user","content":"这电影也太牛了吧"},
        {"role":"assistant","content":"推荐"},
        {"role":"user","content":"有点震惊到我了"},
        {"role":"assistant","content":"推荐"},
        {"role":"user","content":"这电影还想再看一遍"},
        {"role":"assistant","content":"推荐"},
        {"role":"user","content":"这电影感觉也就那样吧"},
        {"role":"assistant","content":"不推荐"},
        {"role":"user","content":"以后不会再来看了"},
        {"role":"assistant","content":"不推荐"},
        {"role":"user","content":"太让我失望了，白来看了"},
        {"role":"assistant","content":"不推荐"},
    ]
    messages=[{"role":"system","content":CLASSIFY_PROMPT}] + examples + [{"role":"user","content":text}]
    try:
        result=generate_response(messages,temperature=0.2)
        print(f"输入的内容：{text}")
        print(f"输出的结果：{result}")
    except Exception as e:
        print(f"api调用发生错误，错误内容为：{e}")
#===========测试区======================
if __name__=="__main__":
    
    classify_review("这片子剧情太拖沓了，看得想睡觉。")
    classify_review("这片子剧情太牛了")
    classify_review("希望从没看过这部电影")
    classify_review("这片子怎么说呢，演员很努力，导演很用心，但看完总觉得少了点什么。")