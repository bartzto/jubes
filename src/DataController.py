import json
import os


class DataController:

    def __init__(self, path):
        self.path = path
        with open(os.path.join(path, 'accounts.json')) as accountfile:
            self.accounts = json.load(accountfile)
        with open(os.path.join(path, 'prices.json')) as pricesfile:
            self.prices = json.load(pricesfile)
        with open(os.path.join(path, 'addfund.json')) as fundfile:
            self.balance = json.load(fundfile)
        

    def getAccountJSON(self):
        return self.accounts

    def getPriceJSON(self):
        return self.prices
    
    def getFundJSON(self):
        return self.balance

    def writeAccountJSON(self, accounts):
        self.accounts = accounts
        self.writeAccountToFile()

    def writeAccountToFile(self):
        with open(os.path.join(self.path, 'accounts.json'), 'w') as outfile:
            json.dump(self.accounts, outfile)

