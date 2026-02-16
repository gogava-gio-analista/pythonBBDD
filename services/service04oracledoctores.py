import oracledb
from models import doctor as model

class ServiceDoctores:
    def __init__(self):
        self.connection = oracledb.connect(
            user="system",
            password="ORACLE",
            dsn="localhost/freepdb1"
        )

    def getDoctores(self):
        cursor = self.connection.cursor()
        sql = "select * from doctor"
        cursor.execute(sql)
        lista = []
        for d in cursor:
            doctor = model.Doctor()
            doctor.hospital_cod = d[0]
            doctor.doctor_no = d[1]
            doctor.apellido = d[2]
            doctor.especialidad = d[3]
            doctor.salario = d[4]
            lista.append(doctor)
        cursor.close()
        return lista
    
    def insertarDoctor(self, hospid, apellido, espec, salario):
        cursor = self.connection.cursor()
        sql = 'select max(doctor_no)+1 as maximo from doctor'
        cursor.execute(sql)
        row = cursor.fetchone()
        id = row[0]
        sql = f'insert into doctor values (:hospid, :doctid, :apellido, :espec, :salario)'
        cursor.execute(sql, (hospid, id, apellido, espec, salario,))
        self.connection.commit()
        cursor.close()

    def updateDoctor(self, hospid, doctid, apellido, espec, salario):
        cursor = self.connection.cursor()
        sql = 'update doctor set hospital_cod=:hospid, apellido=:ape, especialidad=:esp, salario=:sal where doctor_no=:docid'
        cursor.execute(sql, (hospid, apellido, espec, salario, doctid,))
        self.connection.commit()
        cursor.close()

    def deleteDoctor(self, doctid):
        cursor = self.connection.cursor()
        sql = 'delete from doctor where doctor_no=:doctid'
        cursor.execute(sql, (doctid,))
        self.connection.commit()
        cursor.close()