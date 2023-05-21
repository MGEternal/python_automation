import pandas as pd

# สร้าง DataFrame จากข้อมูล


df = pd.read_excel("excel.xls")
filter = df[df['Gender'] == 'Male']
# แสดงข้อมูลใน DataFrame
print(filter)


