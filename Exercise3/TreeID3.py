import math

from FERAICourse2020.Exercise3.trainingSet import *
class TreeID3:

    def __init__(self):
        self._yes: int = 0
        self._no: int = 0
        self._total_entries = 0
        self.attributes_entropy: Dict[str,Dict] = {}
        # temperature
        #           ->hot->average information entropy
        #           ->comfortable->average information entropy
        #           ->cold->average information entropy
        self.average_information_header: Dict[str, float] = {}
        # temperature
        #           ->N.n
        self.gain_header: Dict[str, float] = {}

    def get_attributes_entropy(self) -> Dict[str, Dict]:
        return self.attributes_entropy

    def set_attributes_entropy(self, attributes_entropy: Dict[str, Dict]):
        self.attributes_entropy = attributes_entropy

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

            # calc of attribute individual entropy + average info
            for typeAttribute in attributes_sublist:
                n = self.get_total_entries() - typeAttribute
                p = typeAttribute
                individual_entropy = self.calc_entropy(p, n)


                attributes_sublist[typeAttribute.key] = (((p+n)/(self.get_yes+self.get_no()))*individual_entropy)



            self.attributes_entropy[header] = attributes_sublist

        #calc of average information per header
        for header in self.attributes_entropy:
            header_average: float = 0
            for type in header:
                header_average += type

            self.average_information_header[header.key] = header_average

        #calc of Gain per header
        for header in self.average_information_header:
            self.gain_header[header.key] = general_entropy - header









    def calc_entropy(p: int, n: int) -> float:
        return (-p / (p + n)) * (math.log2(p / (p + n))) - ((n / (p + n)) * (math.log2(n / (p + n))))

