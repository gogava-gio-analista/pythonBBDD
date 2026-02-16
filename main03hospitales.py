from services import service03oraclehospitales as services

#Creamos nuestro servicio de Oracle
service = services.ServiceHospitales()
print("------CRUD Hospitales------")
print("1.- Mostrar hospitales")
print("2.- Insertar hospital")
print("3.- Update hospital")
print("4.- Delete hospital")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    print("Listado de hospitales")
    lista = service.getHospitales()
    for h in lista:
        print(f"Id: {h.idHospital} - {h.nombre} - Camas: {h.camas}")
elif (opcion == 2):
    id = int(input("Id del nuevo hospital: "))
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    tlf = input("Telefono: ")
    camas = int(input("Número de camas: "))
    service.insertarHospital(id, nombre, direccion, tlf, camas)
    print("Insertado OK")
elif (opcion == 3):
    id = int(input("Id del nuevo hospital: "))
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    tlf = input("Telefono: ")
    camas = int(input("Número de camas: "))
    service.updateHospital(id, nombre, direccion, tlf, camas)
    print("Modificado OK")
elif (opcion == 4):
    id = int(input("Id del hospital: "))
    service.deleteHospital(id)
    print('Eliminado OK')
print("Fin de programa")
