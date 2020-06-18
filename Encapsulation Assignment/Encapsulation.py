class Inventory:
    def __init__(self):
        self._inventoryprice = 4.50
        self.__inventorycount = 245

    def getInventoryInfo(self):
        print("Price: {}\nCount: {}\n".format(self._inventoryprice, self.__inventorycount))

    def changeInventoryCount(self, invcount):
        self.__inventorycount = invcount


Product1 = Inventory()
Product1.getInventoryInfo()
Product1.changeInventoryCount(250)
Product1._inventoryprice = 4
Product1.getInventoryInfo()
