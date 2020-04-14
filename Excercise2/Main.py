from FERAICourse2020.Excercise2.Clause import *

if __name__ == '__main__':

    caso = Clause()
    caso.readFile("Files/cooking_examples/chicken_alfredo.txt")
    caso.readFile("Files/cooking_examples/chicken_alfredo_input.txt")
    print(caso.get_atomList())
    print(caso.get_clausesList())
    print(caso.get_instructionsList())