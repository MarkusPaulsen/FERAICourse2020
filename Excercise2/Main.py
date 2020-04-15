from FERAICourse2020.Excercise2.Clause import *

""""""""""""""""
def plResolution()://Sketch
    clause = cnfConvert()
    new = None
    while():
        for clauses in selectClauses(clauses):
            resolvents = plresolver(c1,c2)
            if resolvents.contain("NILL"):
                return true
        if clauses.contein(new)
            return false
        clauses.append(new)

"""""""""""



if __name__ == '__main__':

    caso = Clause()
    caso.readFile("Files/cooking_examples/chicken_alfredo.txt")
    caso.readFile("Files/cooking_examples/chicken_alfredo_input.txt")
    print(caso.get_atomList())
    print(caso.get_clausesList())
    print(caso.get_instructionsList())
