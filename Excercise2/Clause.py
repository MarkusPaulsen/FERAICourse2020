from typing import List, Dict
class Clause:
    def __init__(self):
        self._atomList: List[str] = []
        self._clausesList: List[str] = []
        self._instructionsList: List[str] = []
        self._goalClause: str = ""
    def get_goalClause(self) -> str:
        return self._goalClause

    def set_goalClause(self, goalClause: str):
        self._goalClause = goalClause
    def get_atomList(self) -> List[str]:
        return self._atomList

    def set_instructionsList(self, instructionsList: List[str]):
        self._instructionsList = instructionsList
    def get_instructionsList(self) -> List[str]:
        return self._instructionsList

    def set_atomList(self, atomList: List[str]):
        self._atomList = atomList

    def get_clausesList(self) -> List[str]:
        return self._clausesList

    def set_clausesList(self, clausesList: List[str]):
        self._clausesList = clausesList


    def readFile(self, path: str):
        doc = open(path, encoding="utf8")
        doc_lines: List[str] = doc.readlines()

        if not path.__contains__("input"):
            for line in doc_lines:

                if line.__contains__("#"):
                    continue

                if line.__contains__(" "):#Is a clause
                    if line.__contains__("~v"):
                        print("CONTIENE DISJOINT")
                        line.replace("~v","*")
                        additionalClause: List[str] = (line.split("~v"))
                        for l in additionalClause:
                            self._clausesList.append(l.strip("\n *").lower())
                    else:
                        self._clausesList.append(line.strip("\n*").lower())
                else:
                        self._atomList.append(line.strip("\n*").lower())

            self.set_goalClause(self._clausesList[-1])
            self._clausesList.remove(self.get_goalClause())

        else:
            for line in doc_lines:
                if line.__contains__("#"):
                    continue
                self._instructionsList.append((line.lower()).strip("\n *"))