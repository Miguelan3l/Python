from abc import ABC, abstractmethod
class car_rental(ABC):
    def Milelimit(self, miles):
        print("The miles allowd on your car rental:", miles)
    @abstractmethod
    def milesbought(self, miles):
        pass

class carpayment(car_rental):
    def milesbought(self, miles):
        print('your purchase of miles is {} and the miles you excited was 300miles'.format(miles))
obj = carpayment()
obj.Milelimit('900 miles')
obj.milesbought('900 miles')
