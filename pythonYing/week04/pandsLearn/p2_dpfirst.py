import pandas as pd
import numpy as np
import matplotlib as plt
import os

file = os.path.realpath(__file__)
pwd = os.path.dirname(file)
book = os.path.join(pwd, "book_utf8.csv")

df = pd.read_csv(book)

# print(df)

# 筛选标题为"还行"这一列
df["还行"]

# 切片方式筛选
# 显示前3行
df[:3]

# 增加列名
df.columns = ['star', 'vote', 'shorts']

# 显示特定的行、列
# print(df.loc[1:3, ['star']])

# 过滤数据
df['star'] == '力荐'
# print(df[df['star'] == '力荐'])

# print(df.dropna())


# 数据聚合
# print(df.groupby('star').sum())

# 创建新列
star_to_number = {
    '力荐': 5,
    '推荐': 4,
    '还行': 3,
    '较差': 2,
    '很差': 1
}
df['new_star'] = df['star'].map(star_to_number)

print(df["new_star"])

print(df)
