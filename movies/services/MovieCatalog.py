import os

class MovieCatalog:

    pathFileMovies = "movies.txt"

    @staticmethod
    def addMovie(movie):
        try:
            file = open(MovieCatalog.pathFileMovies, "a")

            file.write(movie.__str__() + "\n")
        except Exception as e:
            print("Exeption in add a Movie", e)
        finally:
            file.close()

    @staticmethod
    def listMovies():
        try:
            file = open(MovieCatalog.pathFileMovies, "r")
            print("Catalogo de Peliculas:")
            print(file.read())
        except Exception as e:
            print("An error is present when the Movie catalog was reed")
        finally:
            file.close()

    @staticmethod
    def deleteMovies():
        try:
            os.remove(MovieCatalog.pathFileMovies)
            print("Archivo eliminado=", MovieCatalog.pathFileMovies)
        except Exception as e:
            print("Ocurrio un erroar al eliminar el archivo de Peliculas", e)

