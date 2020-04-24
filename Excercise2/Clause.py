from typing import *


# noinspection PyMethodMayBeStatic
class Clause:
    def __init__(self):
        self._clauses_list: List[str] = []
        self._goal_clause: str = ""
        self._new_goal_clause: str = ""

    def get_clauses_list(self) -> List[str]:
        return self._clauses_list

    def set_clauses_list(self, clauses_list: List[str]):
        self._clauses_list = clauses_list

    def get_goal_clause(self) -> str:
        return self._goal_clause

    def set_goal_clause(self, goal_clause: str):
        self._goal_clause = goal_clause

    def append_to_clauses_list(self, clause: str):
        if clause not in self._clauses_list:
            self._clauses_list.append(clause)

    def remove_from_clauses_list(self, clause: str):
        if clause in self._clauses_list:
            self._clauses_list.remove(clause)

    def fill_clauses_list(self, input_file_path: str, last_clause_goal: bool):
        input_file = open(input_file_path, encoding="utf8")
        input_file_list: List[str] = input_file.readlines()
        input_file.close()
        for input_file_element in input_file_list:
            if input_file_element.__contains__("#"):
                continue
            # Remove candidate
            if input_file_element.__contains__("~v"):
                sub_clause_list: List[str] = (input_file_element.split("~v"))
                for sub_clause_element in sub_clause_list:
                    self.append_to_clauses_list(clause=sub_clause_element.strip("\n").lower())
            # /Remove candidate
            else:
                self.append_to_clauses_list(clause=input_file_element.strip("\n").lower())
        if last_clause_goal:
            self.set_goal_clause(self._clauses_list[-1])
            self._clauses_list = self._clauses_list[:-1]

    def negate(self, clause: str) -> str:
        clause_atoms: List[str] = clause.split(" ")
        negated_clause: str = ""
        for clause_atom in clause_atoms:
            if clause_atom[0] == "~":
                negated_clause_atom = clause_atom[1:]
            else:
                negated_clause_atom = "~" + clause_atom

            negated_clause += negated_clause_atom + " "
        return negated_clause[:-1]

    def append_clause(self, negated_clause: str):
        if negated_clause.__contains__("~v"):
            sub_clause_list: List[str] = (negated_clause.split("~v"))
            for sub_clause_element in sub_clause_list:
                self.append_to_clauses_list(sub_clause_element.strip("\n").lower())
        else:
            self.append_to_clauses_list(negated_clause.strip("\n").lower())

    def generate_last_clause_atoms(self, last_clause: str) -> List[str]:
        last_clause_atoms: List[str] = []
        if last_clause.__contains__("v"):
            sub_clause_list: List[str] = (last_clause.split("v"))
            for sub_clause_element in sub_clause_list:
                last_clause_atoms.append(sub_clause_element.strip(" "))
        else:
            last_clause_atoms.append(last_clause)
        return last_clause_atoms

    def operate_clauses(self, last_clause: str, enumerator: int) -> (bool, int):
        enumerator_temp: int = enumerator
        last_clause_atoms: List[str] = self.generate_last_clause_atoms(last_clause=last_clause)
        for last_clause_atom in last_clause_atoms:
            negate_last_clause_atom = self.negate(last_clause_atom)
            for clauses_list_element in self._clauses_list:
                if clauses_list_element.__contains__(" " + negate_last_clause_atom) \
                        or clauses_list_element == negate_last_clause_atom:
                    if clauses_list_element.__contains__("v"):
                        if clauses_list_element.__contains__(" v " + negate_last_clause_atom):
                            new_clauses_list_element = clauses_list_element.replace(" v " + negate_last_clause_atom, "")
                        else:
                            new_clauses_list_element = clauses_list_element.replace(negate_last_clause_atom + " v ", "")
                    else:
                        new_clauses_list_element = clauses_list_element.replace(negate_last_clause_atom, "")
                        new_last_clause_atoms = last_clause_atoms.copy()
                        new_last_clause_atoms.remove(last_clause_atom)
                        if new_clauses_list_element == "" and (new_last_clause_atoms == []):
                            new_clauses_list_element = "NIL"
                        elif new_clauses_list_element == "" and (new_last_clause_atoms !=[]):
                            new_clauses_list_element = ""
                            for removed in new_last_clause_atoms:
                                new_clauses_list_element = removed + " v "
                            if new_clauses_list_element != "":
                                new_clauses_list_element = new_clauses_list_element[:-3]

                    print(
                        str(enumerator_temp)
                        + ". " + new_clauses_list_element
                        + " (" + str(self._clauses_list.index(clauses_list_element) + 1)
                        + " , " + str(enumerator_temp - 1)
                        + ")"
                    )
                    enumerator_temp += 1
                    self.append_clause(new_clauses_list_element)
                    if self._clauses_list[-1] == "NIL":
                        return False, enumerator_temp
                    else:
                        self._new_goal_clause = self._clauses_list[-1]
                        return True, enumerator_temp
        return False, enumerator_temp

    def refutation(self):
        enumerator = 1
        for clauses_list_element in self._clauses_list:
            if clauses_list_element != self._goal_clause:
                print(str(enumerator) + ". " + clauses_list_element)
                enumerator += 1
        self._new_goal_clause = self.negate(self._goal_clause)
        print("=============")
        print(str(enumerator) + ". " + self._new_goal_clause)
        enumerator += 1
        print("=============")
        while True:
            not_done_yet, enumerator = self.operate_clauses(self._new_goal_clause, enumerator)
            if not not_done_yet:
                break
        print("=============")
        if not self.get_clauses_list().__contains__("nil"):
            print(self._goal_clause + " is unknown")
        else:
            print(self._goal_clause + " is true")
        self.remove_from_clauses_list("nil")
