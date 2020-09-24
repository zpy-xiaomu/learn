#__author__ = 'zpy'
import os
import openpyxl
new_wb = openpyxl.workbook()
new_ws = new_wb.active
path = r'D:\咪咕文档\资源池查询表'
file_list = os.listdir(path)
#print(file_list)
for file in file_list:
    wb = openpyxl.load_workbook(path + '/'+ file)
    ws = wb.active
    for row in ws.iter_rows(min_row=2,values_only=True):
        new.ws.append(row)
new_wb.save(r'D:\咪咕文档\资源池查询表\1.xlsx')