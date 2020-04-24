from typing import *
from Clause import Clause
from AvailableWorkingModes import AvailableWorkingModes


class CookingAssistant:

    def __init__(self, mode: str, input_file_path: str, query_file_path: str):
        if mode == "cooking_test":
            self.mode: AvailableWorkingModes = AvailableWorkingModes.TEST
        else:
            self.mode: AvailableWorkingModes = AvailableWorkingModes.INTERACTIVE
        self.clause: Clause = Clause()
        self.clause.fill_clauses_list(input_file_path, False)
        self.copy_clauses_list = self.clause.get_clauses_list().copy()
        self.command_list: List[str] = []
        if self.mode == AvailableWorkingModes.TEST:
            self.test_main(query_file_path)
        else:
            self.interactive_main()

    def work(self):
        for command in self.command_list:
            if command[-1] == "?":
                self.clause.set_clauses_list(self.copy_clauses_list.copy())
                self.clause.set_goal_clause(command[:-2])
                self.clause.refutation()
            elif command[-1] == "+":
                self.copy_clauses_list.append(command[:-2])
            elif command[-1] == "-":
                self.copy_clauses_list.remove(command[:-2])
            else:
                print("Broken command")

    def interactive_main(self):
        while True:
            self.command_list = []
            user_input: str = input()
            if user_input == "exit":
                break
            else:
                self.command_list.append(user_input)
                self.work()

    def test_main(self, query_file_path):
        query_file = open(query_file_path, encoding="utf8")
        query_file_list: List[str] = query_file.readlines()
        query_file.close()
        for query_file_element in query_file_list:
            self.command_list.append(query_file_element.strip("\n").lower())
        self.work()





