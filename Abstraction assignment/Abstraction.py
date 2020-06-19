from abc import ABC, abstractmethod


class event(ABC):
    def eventDate(self, date):
        print("This event occurs on {}.".format(date))
    @abstractmethod
    def eventDescription(self, desc_parameter):
        pass

class birthday(event):
    def eventDescription(self, desc_parameter):
        print("It's a birthday, happy birthday {}!".format(desc_parameter))

event1 = birthday()
event1.eventDate("09/24/2020")
event1.eventDescription("Charlie")
