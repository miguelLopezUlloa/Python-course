import pathlib
import os
import re
import glob
import string

class EpamAnalizer:
    FILE_NAME = "EpamHomework.py"
    PATH = 'C:\\Users\\Miguel_Ulloa\\Documents\\Devs\\Python\\Python-course\\homework'

    def __init__(self):
        print("Starting Epam Static Analizer")
        self.totalLines = 0
        #self.tokenDict = { "token00": "import", "token01": "from", "token02": "class", "token03": "def", "token04": "raise"}
        self.tokenDict = {"import": "import", "class": "class", "def": "def",
                          "raise": "raise"}

        #print(self.tokenDict)

    def seachFilesDirectory(self):
        filesList = []

        for dirname, _, filenames in os.walk(
                self.PATH):
            for filename in glob.glob('*.py'):
                filesList.append(os.path.join(dirname, filename))

        return filesList

    def setTotalLines(self, totalLines):
        self.totalLines = totalLines

    def getTotalLines(self):
        return self.totalLines

    def readByLines(self, fileToParse):
        try:
            #archivo = open(self.FILE_NAME)
            archivo = open(fileToParse)

            codeLines = list(filter( lambda archivo: str(archivo.split("\n") and archivo.strip()), archivo))
            firstParsedLines = list(map(lambda item: str(item).lstrip(), codeLines))
            #secondParsedLines = list(filter( lambda item: str(item).startswith('#') , firstParsedLines))
            self.setTotalLines(len(firstParsedLines))
            #print(secondParsedLines)
        finally:
            archivo.close()

        return firstParsedLines

    def count_elements(self,input_list):
        counterTokens = dict.fromkeys(self.tokenDict)

        for llave in counterTokens:
            countKey = 0

            for index in range(len(input_list)):
                if self.verifyStart(input_list[index],llave) == llave:
                    countKey += 1

            counterTokens[llave] = countKey

        #print(counterTokens)
        return counterTokens

    def verifyStart(self, line, token):
        strFound = ""

        if (line.startswith(token)):
            for match in re.findall(token, line):
                strFound = match

        return strFound

    def showPythonStatistics(self, fileToParse, statistics):
        strAllCounters = fileToParse + " " + str(self.getTotalLines())
        lstCounters = list(map(lambda counters: statistics[counters]  , statistics))

        for items in lstCounters:
            strAllCounters += " " + str(items)
           #print('{1} {0}!'.format(items, fileToParse))

        print("\033[1;31m"+ strAllCounters)



    def searchAndParsedLines(self):
        listPythonFiles = self.seachFilesDirectory()

        for fileToParse in listPythonFiles:
            firstParsedLines = self.readByLines(fileToParse)
            counterTokens = dict(self.count_elements(firstParsedLines))
            self.showPythonStatistics(fileToParse,counterTokens)
            #print(counterTokens)

analizer = EpamAnalizer()

analizer.searchAndParsedLines()
