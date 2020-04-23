
from FERAICourse2020.Excercise2.Clause import *



if __name__ == '__main__':

    caso = Clause()
    caso.readFile("Files/resolution_examples/small_example.txt")
    #caso.readFile("Files/resolution_examples/coffee_noheater.txt")

    #caso.readFile("Files/resolution_examples/chicken_alfredo.txt")


    print(caso.get_clausesList())
    print(caso.get_goalClause())
    caso.set_goalClause(caso.negate(caso.get_goalClause()))

    caso.appendClause(caso.get_goalClause())




    while(caso.operateClauses(caso.get_last_clausesList())):
       print(caso.get_clausesList())
    print("############################################\n")
    #caso.operateClauses(caso.get_last_clausesList())
    #caso.operateClauses(caso.get_last_clausesList())
    #print("BIEN\n")
    #caso.operateClauses(caso.get_last_clausesList())
    print(caso.get_clausesList())
    if not caso.get_clausesList().__contains__("nill"):
        print("->UNSOLVED\n")
    else:
        print("->SOLVED\n")

