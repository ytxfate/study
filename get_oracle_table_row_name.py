import cx_Oracle

conn_oracle = cx_Oracle.connect('username', 'password','127.0.0.1:1521/orcl', encoding="UTF-8")     # 不设编码方式时报错 UnicodeDecodeError
cursor_oracle = conn_oracle.cursor()
cursor_oracle.execute("select u.TABLE_NAME,u.NUM_ROWS from user_tables u")
rows = cursor_oracle.fetchall()
tables = {}
for row in rows:
    print(row[0])
    sql_tmp = 'select * from ' + row[0] + ' where rownum = 1'
    cursor_oracle.execute(sql_tmp)
    headers_info = cursor_oracle.description
    table_headers = [i[0] for i in headers_info]
    tables[row[0]] = table_headers
print(len(tables))
with open('aa.txt', 'w') as f:
    f.write(str(tables))
