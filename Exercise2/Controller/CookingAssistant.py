from Clause import Clause
from Model.AvailableWorkingModes import AvailableWorkingModes


class CookingAssistant:

    def __init__(self, input_file_path: str, query_file_path: str):
        self.mode: AvailableWorkingModes = AvailableWorkingModes.INTERACTIVE
        self.clause: Clause = Clause()
        self.clause.read_file(input_file_path, False)




    def interactive_main(self):
        while True:
            user_input: str = input()
            if user_input == "exit":
                break
            elif user_input[-1] == "?":
                pass
            elif user_input[-1] == "+":

                pass
            elif user_input[-1] == "-":
                pass


