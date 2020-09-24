#__author__ = 'zpy'
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
data =[
       ['虚拟机名称','业务说明','DCN地址','业务地址','vCPU','内存（G）','CPU利用率 (%)','内存利用率 (%)'],
       ['ZJHZ-CMREAD-WYSWIKI01-VINT-SD','ZABBIX监控中心 武天宇','10.211.137.134','192.168.23.17','2','8','38.28','59.45']
      ]
for row in data:
    ws.append(row)
wb.save(r'C:\Users\zpy\Desktop\test.xlsx')
