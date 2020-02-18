from Account import Account
from DataController import DataController
from GUIController import GUIController


class InputController:
    def __init__(self, acc: Account, dCont: DataController, gCont: GUIController):
        self.acc = acc
        self.dCont = dCont
        self.gCont = gCont

    def rfidListener(self):
        while True:
            self.gCont.display("Scannen Sie die Karte ein!")
            # TODO read RFID UID
            uid = input()
            self.gCont.display("Bitte wählen Sie den Kaffee aus!")
            self.gCont.showCoffees(self.dCont.getPriceJSON())
            self.buttonListener(uid)

    def buttonListener(self, uid):
        # TODO listen for Button Press
        try:
            button = int(input())
        except ValueError:
            print("Not an integer! Try again.")
            return

        if button < 0 or button >= len(self.dCont.getPriceJSON()):
            self.gCont.display("Dieser Kaffee existiert nicht!")
            return
        self.acc.bookCoffee(uid, button)
