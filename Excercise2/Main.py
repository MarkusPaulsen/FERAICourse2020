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
    caso.readFile("Files/resolution_examples/small_example.txt")


    print(caso.get_clausesList())
    print(caso.get_goalClause())
    caso.negate("~a v b")