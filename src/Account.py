from DataController import DataController
from GUIController import GUIController


class Account:
    def __init__(self, dCon: DataController, gCon: GUIController):
        self.dCon = dCon
        self.gCon = gCon

    def bookCoffee(self, uid, coffee):
        jsonP = self.dCon.getPriceJSON()
        jsonA = self.dCon.getAccountJSON()
        if uid not in jsonA.keys():
            self.gCon.display("Benutzer unbekannt!")
            return
        price = jsonP[coffee]["price"]
        balance = jsonA[uid]["balance"]
        if balance - price < 0:
            self.gCon.display("Ihr Guthaben ist nicht ausreichend!")
        else:
            self.gCon.display("Danke für ihren Einkauf!")
            jsonA[uid]["balance"] = balance - price
            jsonA[uid]["transactions"].append({"type": jsonP[coffee]["name"], "amount": (-1 * jsonP[coffee]["price"])})
            self.dCon.writeAccountJSON(jsonA)
            self.gCon.display("Ihr Guthaben ist: " + str(jsonA[uid]["balance"]) + " €")

