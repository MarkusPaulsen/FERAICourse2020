from typing import *


# noinspection PyMethodMayBeStatic
class Clause:
    def __init__(self):
        self._atom_list: List[str] = []
        self._clauses_list: List[str] = []
        self._instructions_list: List[str] = []
        self._goal_clause: str = ""

    def get_atom_list(self) -> List[str]:
        return self._atom_list

    def set_atom_list(self, atom_list: List[str]):
        self._atom_list = atom_list

    def get_clauses_list(self) -> List[str]:
        return self._clauses_list

    def set_clauses_list(self, clauses_list: List[str]):
        self._clauses_list = clauses_list

    def get_instructions_list(self) -> List[str]:
        return self._instructions_list

    def set_instructions_list(self, instructions_list: List[str]):
        self._instructions_list = instructions_list

    def get_goal_clause(self) -> str:
        return self._goal_clause

    def set_goal_clause(self, goal_clause: str):
        self._goal_clause = goal_clause

    def get_last_clauses_list(self) -> str:
        return self._clauses_list[-1]

    def read_file(self, path: str, last_clause_goal: bool):
        doc = open(path, encoding="utf8")
        doc_lines: List[str] = doc.readlines()
        if not path.__contains__("input"):
            for line in doc_lines:
                if line.__contains__("#"):
                    continue
                if line.__contains__("~v"):
                    print("CONTIENE DISJOINT")
                    line.replace("~v", "*")
                    additional_clause_list: List[str] = (line.split("~v"))
                    for additional_clause_element in additional_clause_list:
                        self._clauses_list.append(additional_clause_element.strip("\n *").lower())
                else:
                    self._clauses_list.append(line.strip("\n*").lower())
                    self._atom_list.append(line.strip("\n*").lower())
            if last_clause_goal:
                self.set_goal_clause(self._clauses_list[-1])
                self._clauses_list.remove(self.get_goal_clause())
        else:
            for line in doc_lines:
                if line.__contains__("#"):
                    continue
                self._instructions_list.append((line.lower()).strip("\n *"))

    def negate(self, exp: str) -> str:
        atoms: List[str] = exp.split(" ")
        print(atoms)
        out: str = ""
        for char in atoms:
            if char.__contains__("~"):
                char = char.replace("~", "")
            else:
                char = char.replace(char, "~" + char)
            if atoms.__contains__("v"):
                out += " " + char
            out += char
            print("-------" + out + "------------\n")
        return out

    def append_clause(self, n_cls: str):
        if n_cls.__contains__("~v"):
            n_cls.replace("~v", "*")
            additional_clause_list: List[str] = (n_cls.split("~v"))

            for additional_clause_element in additional_clause_list:
                self._clauses_list.append(additional_clause_element.strip("\n *").lower())
        else:
            self._clauses_list.append(n_cls.strip("\n*").lower())

    def operate_clauses(self, last_clause: str) -> int:
        atoms_last_clause: List[str] = []
        print("Last clause is --> " + last_clause)
        if last_clause.__contains__("v"):
            atoms_last_clause_temp: List[str] = (last_clause.split("v"))
            for atom in atoms_last_clause_temp:
                atom = atom.strip(" ")
                atoms_last_clause.append(atom)
            print("atomsLastClauselist----> ")
            print(atoms_last_clause)
            print("\n")
        else:
            atoms_last_clause.append(last_clause)
        for items in atoms_last_clause:
            if items.__contains__("~"):
                temp_clasue = items.replace("~", "")
                print("TEMP clause is --> " + temp_clasue)
                for c in self.get_clauses_list():
                    if c.__contains__(" " + temp_clasue) or c == temp_clasue:
                        print("Found--> " + c)
                        if c.__contains__("v"):
                            print("Has v \n")
                            print(c)
                            c = c.replace(" v " + temp_clasue, "")
                            c = c.replace(temp_clasue + " v ", "")
                        c = c.replace(temp_clasue, "")
                        print(c + "*****\n")
                        if c == "":
                            c = "NILL"
                        if c == self._clauses_list[-1]:
                            return 0
                        self.append_clause(c)
                        return 1
            else:
                temp_clasue = "~" + items
                for c in self.get_clauses_list():
                    if c.__contains__(" " + temp_clasue) or c == temp_clasue:
                        if c.__contains__("v"):
                            c = c.replace(" v " + temp_clasue, "")
                            c = c.replace(temp_clasue + " v ", "")
                        c = c.replace(temp_clasue, "")
                        if c == "":
                            c = "NILL"
                        if not c == self._clauses_list[-1]:
                            print("xxxxxxxxxxx REPETIDA\n")
                            self.append_clause(c)
                            return 0

                        self.append_clause(c)
                        return 1
        atoms_last_clause.clear()
