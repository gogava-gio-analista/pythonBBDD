from services import service02oracledepartamentos as sv

# insercion = sv.ServiceDepartamento()
# numero = int(input('inserta id departamento: '))
# nombre = input('nombre departamento: ')
# localidad = input('localidad: ')
# regis = insercion.insertarDepartamento(numero, nombre, localidad)
# print(regis)

eliminacion = sv.ServiceDepartamento()
print('dime que departamento quieres eliminar')
lista = eliminacion.getListaDepartamentos()
contador = 1
for dept in lista:
    print(f'{contador} - {dept.nombre}')
    contador += 1
numero = int(input())
departamentoSeleccionado = lista[numero - 1]
id = departamentoSeleccionado.id
registro = eliminacion.eliminarDepartamento(id)
print(f'se ha eliminado {registro} registro')

# update = sv.ServiceDepartamento()
# id = int(input('dime id de que departamento quieres modificar: '))
# nombre = input('ahora como se va a llamar: ')
# local = input('donde se ha trasladado: ')
# registro = update.updateDepartamento(id, nombre, local)
# print (registro)

# servicio = sv.ServiceDepartamento()
# num = int(input('id a buscar departamento: '))
# dato = servicio.getDept(num)
# print(dato.nombre)
# print(dato.loc)