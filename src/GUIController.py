

class GUIController:
    def display(self, text):
        # TODO GPIO write to Display
        print(text)
        return

    def showCoffees(self, jsonP):
        for i in range(len(jsonP)):
            x = jsonP[i]
            print(str(i) + ": " + x["name"] + " für " + str(x["price"]))

