import oracledb
from models import departamento

class ServiceDepartamento:
    def __init__(self):
        self.connection = oracledb.connect(user = 'system', 
                                           password = 'ORACLE',
                                           dsn = 'LOCALHOST/FREEPDB1')
        
    def insertarDepartamento(self, numero, nombre, localidad):
        cursor = self.connection.cursor()
        sql = 'insert into DEPT values (:num, :nombre, :loc)'
        cursor.execute(sql, (numero, nombre, localidad,))
        self.connection.commit()
        registros = cursor.rowcount
        cursor.close()
        return registros
    
    def eliminarDepartamento(self,id):
        cursor = self.connection.cursor()
        sql = 'delete from dept where dept_no = :id'
        cursor.execute(sql, (id,))
        self.connection.commit()
        registros = cursor.rowcount
        cursor.close()
        return registros
    
    def updateDepartamento(self, id, nombre, localidad):
        cursor = self.connection.cursor()
        sql = 'update dept set dnombre=:nombre, loc=:localidad where dept_no=:id'
        cursor.execute(sql, (nombre, localidad, id,))
        self.connection.commit()
        registros = cursor.rowcount
        cursor.close()
        return registros
    
    def getDept(self, id):
        cursor = self.connection.cursor()
        sql = 'select * from dept where dept_no = :id'
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        dept = departamento.Departamento()
        dept.id = row[0]
        dept.nombre = row[1]
        dept.loc = row[2]
        cursor.close()
        return dept 
    
    def getListaDepartamentos(self):
        cursor = self.connection.cursor()
        sql = 'select * from dept'
        cursor.execute(sql)
        listaDept = []
        for row in cursor:
            dept = departamento.Departamento()
            dept.id = row[0]
            dept.nombre = row[1]
            dept.loc = row[2]
            listaDept.append(dept)
        cursor.close()
        return listaDept 