import math

from FERAICourse2020.Exercise3.trainingSet import *
class TreeID3:

    def __init__(self):
        self._yes: int = 0
        self._no: int = 0


    def get_yes(self) -> int:
        return self._yes

    def set_yes(self, yes: int):
        self._yes = yes

    def get_no(self) -> int:
        return self._no

    def set_no(self, no: int):
        self._no = no

    def entropy_calc(self, training_set:trainingSet):
        self.set_yes(0)
        self.set_no(0)
        total: int = 0
        for entry in training_set.get_entries():

            if entry.get_label():
                self.set_yes(self.get_yes()+1)
            else:
                self.set_no(self.get_no()+1)

        total = self.get_yes() + self.get_no()

        entropy = ((-self.get_yes()/self.get_yes()+self.get_no())*(math.log2(self.get_yes()/self.get_yes()+self.get_no())))-((self.get_no()/self.get_yes()+self.get_no())*(math.log2(self.get_no()/(self.get_yes()+self.get_no()))))