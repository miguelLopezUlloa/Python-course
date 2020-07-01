import os
import glob
import pathlib


# ESTOS SON SOLO METEDOS PARA REFERENCIA Y MODOS DE
# IMPLEMTACION DE ALGUNAS FUNCIONALIDADES
def getFilesNames(self):
    files_dir = pathlib.Path(self.PATH)
    files = [x for x in files_dir.iterdir()]
    print(files)


def readLoopLines(self):
    numberLines = 0
    lineCount = 0
    emptyLines = 0
    totalLines = 0

    try:
        archivo = open(self.FILE_NAME)

        for linea in archivo:
            # print(linea)
            # lineCount += len(re.split("\n", linea))
            totalLines += 1

            if (not linea.startswith('\n')):
                numberLines += 1
            elif not linea.strip():
                emptyLines += 1

        self.setTotalLines(numberLines)

        # print(f"Alternative Line counter: {lineCount}")
        print(f"Empty Lines: {emptyLines}")
        print(f"Total Lines: {totalLines}")

        return self.getTotalLines()

    finally:
        archivo.close()


def seachFilesDirectory(self):
    filesList = []

    for dirname, _, filenames in os.walk(
            self.PATH):
        for filename in glob.glob('*.py'):
            filesList.append(os.path.join(dirname, filename))

            # for filename in filenames:
            #    filesList.append(os.path.join(dirname, filename))

        # all_notebooks = [x for x in pathlib.Path('.').glob('**/*.ipynb')]
        # print(all_notebooks)
        # print(filesList)
    return filesList

def countElements(self, input_list):
    counterTokens = dict.fromkeys(self.tokenDict)

    countKey = 0
    # res = any(ele in input_list for ele in counterTokens.keys())
    for keys, tokens in zip(counterTokens.keys(), input_list):
        if self.verifyStart(tokens, keys) in tokens:
            countKey += 1

    counterTokens[keys] = countKey

    return counterTokens
