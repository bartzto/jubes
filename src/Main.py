from Account import Account
from DataController import DataController
from GUIController import GUIController
from InputController import InputController


class Main:
    def __init__(self):
        dCont = DataController("json")
        gCont = GUIController()
        acc = Account(dCont, gCont)
        self.acc = acc
        self.dCont = dCont
        self.gCont = gCont
        self.iCont = InputController(acc, dCont, gCont)

    def start(self):
        self.iCont.rfidListener()


main = Main()
main.start()
