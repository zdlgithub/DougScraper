import openpyxl,os
filepath = os.path.join(os.path.dirname(__file__),'shopee.xlsx')
wb = openpyxl.load_workbook(filepath)
#切换到目标数据表
#ws = wb[]
ws = wb['Sheet1']
#待填充数据
data = [[1,2,3],[4,5,6]]
for x in data:
    ws.append(x)
savename = 'update_excel.xlsx'
wb.save(savename)
