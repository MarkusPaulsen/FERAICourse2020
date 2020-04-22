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

    def get_last_clausesList(self) -> List[str]:
        return self._clausesList[-1]

    def set_clausesList(self, clausesList: List[str]):
        self._clausesList = clausesList


    def readFile(self, path: str):
        doc = open(path, encoding="utf8")
        doc_lines: List[str] = doc.readlines()

        if not path.__contains__("input"):
            for line in doc_lines:

                if line.__contains__("#"):
                    continue

                if line.__contains__("~v"):
                    print("CONTIENE DISJOINT")
                    line.replace("~v","*")
                    additionalClause: List[str] = (line.split("~v"))
                    for l in additionalClause:
                        self._clausesList.append(l.strip("\n *").lower())
                else:
                    self._clausesList.append(line.strip("\n*").lower())

                    self._atomList.append(line.strip("\n*").lower())

            self.set_goalClause(self._clausesList[-1])
            self._clausesList.remove(self.get_goalClause())

        else:
            for line in doc_lines:
                if line.__contains__("#"):
                    continue
                self._instructionsList.append((line.lower()).strip("\n *"))


    def negate(self, exp: str)-> str:
        atoms: str = exp.split(" ")
        print(atoms)
        out: str=""
        for char in atoms:
            if char.__contains__("~"):
                char = char.replace("~","")
            else:
                char = char.replace(char, "~"+char)
            if atoms.__contains__("v"):
                out+=" "+char
            out +=char
            print("-------"+out+"------------\n")
        return out


    def appendClause(self, n_cls: str):
        if n_cls.__contains__("~v"):
            n_cls.replace("~v", "*")
            additionalClause: List[str] = (n_cls.split("~v"))

            for l in additionalClause:
                self._clausesList.append(l.strip("\n *").lower())
        else:
            self._clausesList.append(n_cls.strip("\n*").lower())
            
    def operateClauses(self, lastClause: str)-> int:
        atomsLastClause: List[str] = []
        print("Last clause is --> " + lastClause)
        if(lastClause.__contains__("v")):
            atomsLastClausetemp: List[str] = (lastClause.split("v"))
            for atom in atomsLastClausetemp:
                atom=atom.strip(" ")
                atomsLastClause.append(atom)
            print("atomsLastClauselist----> ")
            print(atomsLastClause)
            print("\n")
        else:
            atomsLastClause.append(lastClause)
        for items in atomsLastClause:
            if items.__contains__("~"):
                tempClasue = items.replace("~","")
                print("TEMP clause is --> " + tempClasue)
                for c in self.get_clausesList():
                    if c.__contains__(" "+tempClasue) or c==tempClasue:
                        print("Found--> "+c)
                        if c.__contains__("v"):
                            print("Has v \n")
                            print(c)
                            c= c.replace(" v "+tempClasue,"")
                            c = c.replace(tempClasue +" v " , "")
                        c = c.replace(tempClasue, "")
                        print(c+"*****\n")
                        if c=="" :
                            c="NILL"
                        if c == self._clausesList[-1]:
                            return 0
                        self.appendClause(c)
                        return 1

                        break
            else:
                tempClasue = "~"+items
                for c in self.get_clausesList():
                    if c.__contains__(" "+tempClasue) or c==tempClasue:
                        if c.__contains__("v"):
                            c = c.replace(" v " + tempClasue, "")
                            c = c.replace(tempClasue + " v ", "")
                        c = c.replace(tempClasue, "")
                        if c == "":
                            c = "NILL"
                        if not c == self._clausesList[-1]:
                            print("xxxxxxxxxxx REPETIDA\n")
                            self.appendClause(c)
                            return 0



                        self.appendClause(c)
                        return 1
                        break
        atomsLastClause.clear()