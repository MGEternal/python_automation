import pandas as pd

# สร้าง DataFrame จากข้อมูล


df = pd.read_excel("excel.xls")
df.loc[df['Id'] == 2587, 'Age'] = 22
df.to_excel('new_excel.xlsx', index=False)
# แสดงข้อมูลใน DataFrame หลังจากแก้ไข
print(df)
