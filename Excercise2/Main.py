from Clause import *


class Main:
    def __init__(self, path: str):
        caso = Clause()
        caso.read_file(path, True)
        caso.set_goal_clause(caso.negate(caso.get_goal_clause()))
        while caso.operate_clauses(caso.get_last_clauses_list()):
            print(caso.get_clauses_list())
        print("############################################\n")

        print(caso.get_clauses_list())
        if not caso.get_clauses_list().__contains__("nill"):
            print("->UNSOLVED\n")
        else:
            print("->SOLVED\n")


if __name__ == '__main__':
    x = Main("Files/resolution_examples/small_example.txt")

    # caso = Clause()
    # caso.readFile("Files/resolution_examples/small_example.txt")
    # # caso.readFile("Files/resolution_examples/coffee_noheater.txt")
    #
    # print(caso.get_clausesList())
    # print(caso.get_goalClause())
    # # caso.appendClause(caso.negate("~a v b"))
    # caso.set_goalClause(caso.negate(caso.get_goalClause()))
    #
    # caso.appendClause(caso.get_goalClause())
    #
    # while (caso.operateClauses(caso.get_last_clausesList())):
    #     print(caso.get_clausesList())
    # print("############################################\n")
    #
    # print(caso.get_clausesList())
    # if not caso.get_clausesList().__contains__("nill"):
    #     print("->UNSOLVED\n")
    # else:
    #     print("->SOLVED\n")
