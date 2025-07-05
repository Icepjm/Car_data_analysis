import pandas as pd
from sqlalchemy import create_engine

# 配置数据库连接
db_config = {
    'host': '192.168.44.161',
    'user': 'root',
    'password': 'root',
    'database': 'car_sales_db'
}
# 创建数据库引擎
engine = create_engine(
    f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}?")

# 表名
table_name = 'car_sales'
# table_name = 'data'

# 导出为CSV
try:
    # 读取整个表到DataFrame
    df = pd.read_sql_table(table_name, engine)

    # 保存为CSV文件
    csv_file = f'{table_name}.csv'
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')  # utf-8-sig支持Excel正确显示中文

    print(f"成功导出表 {table_name} 到 {csv_file}")
except Exception as e:
    print(f"导出失败: {e}")