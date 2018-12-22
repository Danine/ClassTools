import os
import re
import xlrd#excel read
mp = {}#建立字典让学号对应姓名
IDs = []
def prepare():
	excel = xlrd.open_workbook(u"C:/Users/Tyson/Desktop/学校事务/4班事务/4班名单(大三版).xlsx")#数据表格
	sheet = excel.sheet_by_index(0)#表1
	nrows = sheet.nrows#获取行总数
	for i in range(1, nrows):#排除表头
		sid = sheet.cell(i, 0).value#cell:列
		sname = sheet.cell(i, 1).value
		mp[sid] = sname

def rename(path):
	files = os.listdir(path)
	for filename in files:
		oldname = path + filename#加上path为绝对地址
		portion = os.path.splitext(filename)#分割路径，返回路径名和文件扩展名的元组
		if portion[1] == '.docx' or portion[1] == '.doc':#只处理docx和doc格式
			tempID = re.match('.*(201[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]).*',portion[0])
			ID = tempID.group(1)
			IDs.append(ID)
			newname = path + ID + '_' + mp[ID] + u'_4班' + portion[1]#新的文件名，每次不同
			os.rename(oldname, newname)
	return ID

def notfound(ID,IDs):
	for ID in mp:#遍历所有学号
		if not(ID in IDs):#学号不在文件中
			print(mp[ID])#打印字典中对应的名字

if __name__== "__main__":
	path = u"C:/Users/Tyson/Desktop/test1/"#作业地址
	prepare()
	ID = rename(path)
	notfound(ID,IDs)
