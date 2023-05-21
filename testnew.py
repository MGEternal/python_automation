import pandas as pd

# สร้าง DataFrame จากข้อมูล


df = pd.read_excel("new_excel.xlsx")
filtered_data = df[df['Id'] == 1562]
# แสดงข้อมูลใน DataFrame
print(f"{filtered_data['First Name'].values}   {filtered_data['Last Name'].values}")
#print(filtered_data['Age'])


