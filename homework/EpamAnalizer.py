import pathlib
import os
import re
import glob
import string


class EpamAnalizer:
    # FILE_NAME = "EpamHomework.py"
    PATH = 'C:\\Users\\Miguel_Ulloa\\Documents\\Devs\\Python\\Python-course\\homework'
    CURRENT_PATH = os.getcwd()

    def __init__(self):
        print("Starting Epam Static Analizer")
        self.totalLines = 0
        self.tokenDict = {"import": "import", "class": "class", "def": "def",
                          "raise": "raise"}

    # Search all Files to analize in a Directory
    def seachFilesDirectory(self):
        filesList = []

        for dirname, _, filenames in os.walk(
                self.CURRENT_PATH):
            for filename in glob.glob('*.py'):
                filesList.append(os.path.join(dirname, filename))

        return filesList

    def setTotalLines(self, totalLines):
        self.totalLines = totalLines

    def getTotalLines(self):
        return self.totalLines

    # Read the File to analize by line
    def readByLines(self, fileToParse):
        try:
            archivo = open(fileToParse)

            codeLines = list(filter(lambda archivo: str(archivo.split("\n") and archivo.strip()), archivo))
            firstParsedLines = list(map(lambda item: str(item).lstrip(), codeLines))
            secondParsedLines = self.removeComments(firstParsedLines)

            self.setTotalLines(len(secondParsedLines))
        finally:
            archivo.close()

        return firstParsedLines

    # Remove ALL comment lines like this
    def removeComments(self, firstParsedLines):
        lstFinal = list()

        for index in range(len(firstParsedLines)):
            strItem = str(firstParsedLines[index])
            if not(strItem.startswith("#")):
                lstFinal.append(strItem)

        return lstFinal

    # Token counter with coincident in the Token Dictionary
    def count_elements(self, input_list):
        counterTokens = dict.fromkeys(self.tokenDict)

        for llave in counterTokens:
            countKey = 0

            for index in range(len(input_list)):
                if self.searchStarter(input_list[index], llave) == llave:
                    countKey += 1

            counterTokens[llave] = countKey

        return counterTokens

    # search for the Starter string in the lined
    def searchStarter(self, line, token):
        strFound = ""

        if (line.startswith(token)):
            for match in re.findall(token, line):
                strFound = match

        return strFound
    # show the Staticstics for the Static Analizer in a Python files
    def showPythonStatistics(self, fileToParse, statistics):
        lstColumns = ["Imports:", "Classes:", "Method:", "Error:"]

        strAllCounters = fileToParse + " Lines:" + str(self.getTotalLines())
        lstCounters = list(map(lambda counters: statistics[counters], statistics))

        # for keys,items in statistics.items():
        #    strAllCounters += " " + keys + ":" + str
        for keys, counters in zip(lstColumns, lstCounters):
            strAllCounters += " " + keys + str(counters)

        print("\033[1;31m" + strAllCounters)

    # Main Method to Call the entire Flow for Static Analizer
    def searchAndParsedLines(self):
        listPythonFiles = self.seachFilesDirectory()

        for fileToParse in listPythonFiles:
            firstParsedLines = self.readByLines(fileToParse)
            counterTokens = dict(self.count_elements(firstParsedLines))
            self.showPythonStatistics(fileToParse, counterTokens)

# Create the instance and start the Python search to analize
# and detect the tokens in the dictionary
analizer = EpamAnalizer()
analizer.searchAndParsedLines()

