
class Movie:

    def __init__(self, title=None):
        self.__title = title

    def __str__(self):
        titleMovie= self.__title
        return titleMovie

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title