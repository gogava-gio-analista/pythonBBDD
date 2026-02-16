from services import service04oracledoctores as services

service = services.ServiceDoctores()

def mostrarDoctores():
    lista = service.getDoctores()
    print('La tabla de doctor')
    for i in lista:
        print(i.hospital_cod, i.doctor_no, i.apellido, i.especialidad, i.salario)

print("------CRUD Doctor------")
print("1.- Mostrar Doctor")
print("2.- Insertar Docotor")
print("3.- Update Doctor")
print("4.- Delete Doctor")
print("Seleccione una opción")
opcion = int(input())

if opcion == 1:
    mostrarDoctores()
elif opcion == 2:
    hospid = int(input('Id de hospital: '))
    apellido = input('Apellido: ')
    espec = input('Especialidad: ')
    salario = int(input('Salario: '))
    service.insertarDoctor(hospid, apellido, espec, salario)
    print('Insertado')
    mostrarDoctores()
elif opcion == 3:
    doctid = int(input('Id de doctor: '))
    hospid = int(input('Id de hospital: '))
    apellido = input('Apellido: ')
    espec = input('Especialidad: ')
    salario = int(input('Salario: '))
    service.updateDoctor(hospid, doctid, apellido, espec, salario)
    print('Modificado')
    mostrarDoctores()
elif opcion == 4:
    doctid = int(input('Id de doctor: '))
    service.deleteDoctor(doctid)
    print('Eliminado')
    mostrarDoctores()