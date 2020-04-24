import sys

from CookingAssistant import CookingAssistant


class Main:
    def __init__(self):
        ca = CookingAssistant(sys.argv[1], sys.argv[2], sys.argv[3])



if __name__ == '__main__':
     x = Main()
