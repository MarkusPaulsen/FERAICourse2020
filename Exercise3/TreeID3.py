import math

from FERAICourse2020.Exercise3.trainingSet import *
class TreeID3:

    def __init__(self):
        self._yes: int = 0
        self._no: int = 0
        self._total_entries = 0
        self.attributes: Dict[str,Dict] = {}
        # temperature
        #           ->hot->entropy
        #           ->comfortable->entropy
        #           ->cold->entropy
        

    def get_attributes(self) -> Dict[str, Dict]:
        return self._attributes

    def set_attributes(self, attributes: Dict[str, Dict]):
        self._attributes = attributes

    def get_yes(self) -> int:
        return self._yes

    def set_yes(self, yes: int):
        self._yes = yes

    def get_no(self) -> int:
        return self._no

    def set_no(self, no: int):
        self._no = no

    def get_total_entries(self) -> int:
        return self._total_entries

    def set_total_entries(self, total_entries: int):
        self._total_entries = total_entries

    def entropy(self, training_set: trainingSet):
        self.set_yes(0)
        self.set_no(0)
        total_entries: int = 0
        for entry in training_set.get_entries():

            if entry.get_label():
                self.set_yes(self.get_yes()+1)
            else:
                self.set_no(self.get_no()+1)

        total_entries = self.get_yes() + self.get_no()

        general_entropy = self.calc_entropy(self.get_yes(), self.get_no())

        #calc of positive tags for each atribute type
        index: int = 0
        for header in training_set.get_headers():
            index += 1
            # for each header
            attributes_sublist: Dict[str,float] = {} # pair entry / n Yes
            for entry in training_set.get_entries():
                #for each row
                if entry.get_label():
                    attributes_sublist[entry.row[index]] += 1
                else:
                    attributes_sublist[entry.row[index]] += 0

            # calc of attribute individual entropy
            for typeAttribute in attributes_sublist:
                n = self.get_total_entries() - typeAttribute
                attributes_sublist[typeAttribute.key] = self.calc_entropy(typeAttribute, n)

            self.attributes[header] = attributes_sublist













    def calc_entropy(p: int, n: int) -> float:
        return (-p / (p + n)) * (math.log2(p / (p + n))) - ((n / (p + n)) * (math.log2(n / (p + n))))

