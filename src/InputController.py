import time
from Account import Account
from DataController import DataController
from GUIController import GUIController
from RFIDReader import RFIDReader


class InputController:
    def __init__(self, acc: Account, dCont: DataController, gCont: GUIController):
        self.acc = acc
        self.dCont = dCont
        self.gCont = gCont
        self.rfid = RFIDReader()

    def rfidListener(self):
        while True:
            self.gCont.display("Scannen Sie die Karte ein!")
            uid = self.rfid.read()
            if uid == "233,71,198,72":
                self.gCont.display("Scannen sie die Karte, die sie aufladen möchten.")
                time.sleep(5)
                fundcard = self.rfid.read()
                if uid == "233,71,198,72":
                    
                self.gCont.display("Bitte wählen Sie aus wie viel Guthaben sie aufladen möchten.")
                self.gCont.showFunds(self.dCont.getFundJSON())
                self.buttonListenerFund(fundcard)
            else:
                self.gCont.display("Bitte wählen Sie den Kaffee aus!")
                self.gCont.showCoffees(self.dCont.getPriceJSON())
                self.buttonListenerCoffee(uid)

    def buttonListenerCoffee(self, uid):
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
    
    def buttonListenerFund(self, uid):
        try:
            button = int(input())
        except ValueError:
            print("Not an integer! Try again.")
            return
        
        if button < 0 or button >= len(self.dCont.getFundJSON()):
            self.gCont.display("Diese Buchung existiert nicht!")
            return
        self.acc.addBalance(uid, button)
