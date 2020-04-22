from FERAICourse2020.Excercise2.Clause import *



if __name__ == '__main__':

    caso = Clause()
    caso.readFile("Files/resolution_examples/small_example.txt")
    #caso.readFile("Files/resolution_examples/coffee_noheater.txt")


    print(caso.get_clausesList())
    print(caso.get_goalClause())
    #caso.appendClause(caso.negate("~a v b"))
    caso.set_goalClause(caso.negate(caso.get_goalClause()))

    caso.appendClause(caso.get_goalClause())




    while(caso.operateClauses(caso.get_last_clausesList())):
        print(caso.get_clausesList())
    print("############################################\n")

    print(caso.get_clausesList())
    if not caso.get_clausesList().__contains__("nill"):
        print("->UNSOLVED\n")
    else:
        print("->SOLVED\n")

