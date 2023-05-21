import pandas as pd

# สร้าง DataFrame จากข้อมูล
data = {'ชื่อ': ['John', 'Anna', 'Peter', 'Linda'],
        'อายุ': [25, 30, 35, 40],
        'เงินเดือน': [50000, 60000, 70000, 80000]}

df = pd.read_excel("excel.xls")

# แสดงข้อมูลใน DataFrame
print(df)


