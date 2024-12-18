class CAutores:
    def __init__(self, nombre, apellido, nacionalidad, mejor_obra, anio_publicacion, edad_publicacion):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.mejor_obra = mejor_obra
        self.anio_publicacion = anio_publicacion
        self.edad_publicacion = edad_publicacion

# Lista de autores con sus datos
autores = [
    CAutores("Gabriel", "García Márquez", "Colombiano", "Cien años de soledad", 1967, 40),
    CAutores("Julio", "Cortázar", "Argentino", "Rayuela", 1963, 48),
    CAutores("Isabel", "Allende", "Chilena", "La casa de los espíritus", 1982, 40),
    CAutores("Jorge Luis", "Borges", "Argentino", "Ficciones", 1944, 45),
    CAutores("Clarice", "Lispector", "Brasileña", "La hora de la estrella", 1977, 56),
    CAutores("Juan", "Rulfo", "Mexicano", "Pedro Páramo", 1955, 38),
    CAutores("Carlos", "Fuentes", "Mexicano", "La región más transparente", 1958, 29),
    CAutores("Eduardo", "Galeano", "Uruguayo", "Las venas abiertas de América Latina", 1971, 31)
]

# a. Listar todos los autores de nacionalidad argentina
argentinos = [autor for autor in autores if autor.nacionalidad == "Argentino"]
print("Autores argentinos:")
for autor in argentinos:
    print(f"{autor.nombre} {autor.apellido}")

# b. Listar todos los autores que publicaron entre 1960 y 1980
autores_1960_1980 = [autor for autor in autores if 1960 <= autor.anio_publicacion <= 1980]
print("\nAutores que publicaron entre 1960 y 1980:")
for autor in autores_1960_1980:
    print(f"{autor.nombre} {autor.apellido}: {autor.mejor_obra} ({autor.anio_publicacion})")

# c. Mostrar el promedio de la edad de publicación
promedio_edad = sum(autor.edad_publicacion for autor in autores) / len(autores)
print(f"\nPromedio de edad de publicación: {promedio_edad:.2f} años")

# d. Mostrar todos los autores
print("\nLista completa de autores:")
for autor in autores:
    print(f"{autor.nombre} {autor.apellido}, Nacionalidad: {autor.nacionalidad}, Obra: {autor.mejor_obra}, Año: {autor.anio_publicacion}, Edad: {autor.edad_publicacion} años")
