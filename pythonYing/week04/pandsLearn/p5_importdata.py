import pymysql
import pandas as pd


excel1 = pd.read_excel(r'1.xlsx')

# 指定导入哪个Sheet
pd.read_excel(r'1.xlsx', sheet_name=0)


# 支持其他常见类型
pd.read_csv(r'book_utf8.csv',
            sep=' ',
            nrow=10,
            encoding='utf-8')

pd.read_table(r'file.txt', sep=' ')


sql = 'SELECT *  FROM tb1'
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',  # 使用自己的用户名
    passwd='1qaz@WSX',  # 使用自己的密码
    db='test',  # 数据库名
    charset='utf8'
)
df = pd.read_sql(sql, conn)



excel1.head(1)

# 获取表格的行列数量
excel1.shape

excel1.info()
excel1.describe()
