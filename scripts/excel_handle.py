import pandas as pd
import os
# ===================== 1. 读取测试用例表格 =====================
# 读取本地 Excel 测试数据集
df=pd.read_excel("./test_data/prompt_test_cases.xlsx")
print("===浏览前五行数据===")
print(df.head())
print("\n数据集列名：",df.columns.tolist())
print(f"总测试用例数量：{len(df)}")
# ===================== 2. 基础数据清洗 =====================
# 2.1 删除问题、标准回答为空的无效用例
df_clean=df.dropna(subset=["测试问题","标准回答"])
# print("文件完整路径：", os.path.abspath("df_clean.xlsx"))
print("清理后的数据：\n")
print(df_clean)
# print(df)
# 2.2 按用例ID去重，避免重复测试
df_clean=df_clean.drop_duplicates(subset=["用例ID"])
print("去重过后的数据：\n")
print(df_clean)
# 2.3 重置行索引，保证序号连续
df_clean=df_clean.reset_index(drop=True)
print("重置后的数据：\n")
print(df_clean)
print(f"\n清洗前：{len(df)} 条，清洗后：{len(df_clean)} 条有效用例")
# ===================== 3. 条件筛选（评测核心操作） =====================
# 筛选1：得分低于60分的失败用例，用于后续优化Prompt
fail_case=df_clean[df_clean["得分"]<60]
print("筛选低于60分过后的数据:\n")
print(fail_case)
# 筛选2：v1版本提示词的所有测试结果，用于版本对比
v1_case=df_clean[df_clean["Prompt版本"]=="v1"]
print("v1版本提示词的所有测试结果:\n")
print(v1_case)
# 筛选3：得分在80分以上、且标记为通过的优质用例，用于沉淀少样本示例
good_case=df_clean[(df_clean["得分"] > 80) &  (df_clean["是否通过"]=="是")]
print("得分在80分以上、且标记为通过的优质用例:\n")
print(good_case)


# print("\n=== 失败用例清单（需优化Prompt） ===")
# print(fail_case[["用例ID", "测试问题", "得分"]])

# print("\n=== 优质用例清单（可作为Few-Shot示例） ===")
# print(good_case[["用例ID", "测试问题", "标准回答"]])

# ===================== 4. 导出结果文件 =====================
# 导出失败用例，用于后续迭代优化
fail_case.to_excel("./test_data/待优化用例.xlsx",index=False)
# 导出优质用例，可直接复用为 Few-Shot 素材
good_case.to_excel("./test_data/优秀用例.xlsx",index=False)
print("\n✅ 处理完成，结果已导出到 test_data 目录")