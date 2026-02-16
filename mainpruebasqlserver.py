import mssql_python

connection = mssql_python.connect('Server=sqlpaco3430.database.windows.net;Database=AZURETAJAMAR;Encrypt=yes;UID=adminsql;PWD=Admin123;TrustServerCertificate=yes')
sql = 'select * from emp'
cursor = connection.cursor()
cursor.execute(sql)
for row in cursor:
    print(row[1])
cursor.close()
connection.close()