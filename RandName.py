import xlrd
import random
names = []
excel = xlrd.open_workbook(u"C:/Users/Tyson/\
Desktop/学校事务/4班事务/签到表.xlsx")
sheet = excel.sheet_by_index(0)
nrows = sheet.nrows
for i in range(2, nrows):
    name = sheet.cell(i, 1).value
    names.append(name)

lucky = random.sample(names, 3)
print(lucky)
