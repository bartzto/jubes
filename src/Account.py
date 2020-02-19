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
            jsonA[uid]["balance"] = round(balance - price, 2)
            jsonA[uid]["transactions"].append({"type": jsonP[coffee]["name"], "amount": (-1 * jsonP[coffee]["price"])})
            self.dCon.writeAccountJSON(jsonA)
            self.gCon.display("Ihr Guthaben ist: " + str(jsonA[uid]["balance"]) + " €")
        

    def addBalance(self, uid, category):
        jsonF = self.dCon.getFundJSON()
        jsonA = self.dCon.getAccountJSON()
        if uid not in jsonA.keys():
            self.gCon.display("Benutzer unbekannt!")
            return
        fund = jsonF[category]["balance"]
        wallet = jsonA[uid]["balance"]
        jsonA[uid]["balance"] = wallet + fund
        self.dCon.writeAccountJSON(jsonA)
        self.gCon.display("Ihr Guthaben wurde um " + str(jsonF[category]["balance"]) + "€ aufgeladen")