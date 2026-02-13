from models import mascota

def getSaludo():
    return 'Hoy es juernes'

def getMascota():
    dato = mascota.Mascota()
    dato.nombre = 'Flounder'
    dato.raza = 'Pez'
    dato.edad = 22
    return dato

def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = 'Nala'
    dato.raza = 'Leona'
    dato.edad = 18
    return dato 

def getListaMascotas():
    listaMascotas = []
    dato = mascota.Mascota()
    dato.nombre = 'leona'
    dato.raza = 'perro'
    dato.edad = 12 
    listaMascotas.append(dato)
    