from services import service01prueba

texto = service01prueba.getSaludo()
print(texto)

pez = service01prueba.getMascota()
leona = service01prueba.getMascota2()

print(f'{pez.nombre}, Raza: {pez.raza}')
print(leona.nombre)