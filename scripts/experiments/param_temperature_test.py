#===============温度参数测试=================
from app.llm.client import test_temperature

if __name__ == "__main__":
    # 定义一个需要创意的提问
    my_prompt = "请用一句话描述夏天的感觉，要求使用比喻的修辞手法。"
    
    # 分别用低温和高温调用
    test_temperature(my_prompt, 0.2)  # 低温：输出更确定、更保守[reference:4][reference:5]
    test_temperature(my_prompt, 1.1)  # 高温：输出更具随机性和创造性[reference:6][reference:7]