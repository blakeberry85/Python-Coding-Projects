

class Property:
    address = 'Not listed'
    price = 'N/A'
    rooms = 'N/A'
    sqft = 'N/A'

    def getPropertyInfo(self):
        print("\nAddress: {}\nPrice: {}\nRooms: {}\nArea(Sqft): {}".format(self.address,self.price,self.rooms,self.sqft))

class House(Property):
    floors = 'N/A'
    neighborhood = 'Not listed'

    def getPropertyInfo(self):
        print("\nAddress: {}\nPrice: {}\nRooms: {}\nArea(Sqft): {}\nFloors: {}\nNeighborhood: {}".format(self.address,self.price,self.rooms,self.sqft,self.floors,self.neighborhood))

class Apartment(Property):
    aptnumber = 'N/A'
    aptcomplex = 'Not listed'

    def getPropertyInfo(self):
        print("\nAddress: {}\nPrice: {}\nRooms: {}\nArea(Sqft): {}\nApartment #: {}\nApartment Complex: {}  ".format(self.address,self.price,self.rooms,self.sqft,self.aptnumber,self.aptcomplex))




if __name__ == "__main__":
    house = House()
    house.getPropertyInfo()

    apartment = Apartment()
    apartment.getPropertyInfo()
    
