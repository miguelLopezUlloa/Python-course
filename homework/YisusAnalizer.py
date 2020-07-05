import glob, os


def review_python_files(path):
    os.chdir(path)
    for file_name in glob.glob("*.py"):
        validate_file(path, file_name)


def validate_file(path, file_name):
    code_lines = 0
    dependencies = 0
    classes = 0
    functions = 0
    r_exeptions = 0;
    open_file = open(file_name, "r")
    for line in open_file:
        line = line.strip(' \t\n\r')
        code_lines += 1
        classes += find_words(line, "class")
        functions += find_words(line, "def ")
        dependencies += find_words(line, "import ")
        r_exeptions += find_words(line, "raise")
    open_file.close()
    print(path + file_name + ' Lines ' + str(code_lines) + ' Classes ' + str(classes) + ' Functions ' + str(functions)
          + ' Error ' + str(r_exeptions))


def find_words(line, word):
    is_class = line.find(word)
    if is_class == 0:
        return 1;
    else:
        return 0;

review_python_files("C:\\Users\\Miguel_Ulloa\\Documents\\Devs\\Python\\Python-course\\homework")


