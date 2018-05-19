from openpyxl import Workbook

wb = Workbook()
ws = wb.active
row = ['资源名称', '网盘网址']
ws.append(row)
row2 = ['asdasd', '1231231223']
ws.append(row2)
wb.save(r'D:\{name}.xlsx'.format(name='测试2'))