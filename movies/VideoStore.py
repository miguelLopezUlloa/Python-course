from movies.components.Movie import Movie
from movies.services.MovieCatalog import MovieCatalog

opcion = None

while opcion != "4":
    print("Opciones:")
    print("1. Agregar Pelicula")
    print("2. Listar Peliculas")
    print("3. Eliminar Catalogo de Peliculas")
    print("4. Salir")
    opcion = input("Escribe tu opcion:")

    if opcion == "1":
        movieTitle = input("Introduce el Titulo de la Pelicula:")
        movie = Movie(movieTitle)
        MovieCatalog.addMovie(movie)
    elif opcion == "2":
        MovieCatalog.listMovies()
    elif opcion == "3":
        MovieCatalog.deleteMovies()

else:
    print("Salimos del Video Store")