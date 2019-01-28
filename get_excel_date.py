import xlrd
import json

# 读取 Excel 文件
excel_table = xlrd.open_workbook('DataToRedis.xls')
# 获得 Excel 下标sheet页
sheets = excel_table.sheets()
for sheet in sheets:
    sheet_name = (sheet.name)[:4]
    if sheet_name == '字典目录':
        continue
    # sheet_name = (sheet.name)
    print(sheet_name)
    nrows = sheet.nrows   #行数
    ncols = sheet.ncols   #列数
    with open(sheet_name+".txt", 'w', encoding='utf-8') as f:
        dict_tmp = {}
        for i in range(nrows):
            list_tmp = sheet.row_values(i)
            if list_tmp[0] == '代码':
                continue
            if isinstance(list_tmp[0],int):
                list_tmp[0] = str(list_tmp[0])
            if isinstance(list_tmp[0], float):
                list_tmp[0] = str(int(list_tmp[0]))
            dict_tmp[list_tmp[0]] = list_tmp[1]
        f.write(json.dumps(dict_tmp))
