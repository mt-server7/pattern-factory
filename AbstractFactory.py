from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractManufacturer(ABC):
    @abstractmethod
    def create_coffee(self):
        pass
    
    @abstractmethod
    def create_tea(self):
        pass
    
    @abstractmethod
    def create_water(self):
        pass

class ConcreteManufacturer1(AbstractManufacturer):
    def create_coffee(self):
        return CoffeeBlack()
    
    def create_tea(self):
        return TeaBlack()
    
    def create_water(self):
        return WaterSimple()
    
class ConcreteManufacturer2(AbstractManufacturer):
    def create_coffee(self):
        return CoffeeMilk()
    
    def create_tea(self):
        return TeaGreen()
    
    def create_water(self):
        return WaterMinerale()

class AbstractCoffee(ABC):
    @abstractmethod
    def useful_coffee(self):
        pass

class AbstractTea(ABC):
    @abstractmethod
    def useful_tea(self):
        pass

class AbstractWater(ABC):
    @abstractmethod
    def useful_water(self):
        pass

class CoffeeBlack(AbstractCoffee):
    def useful_coffee(self):
        return 'Вы заказали черный кофе'
    
class CoffeeMilk(AbstractCoffee):
    def useful_coffee(self):
        return 'Вы заказали кофе с молоком'
    
class TeaBlack(AbstractTea):
    def useful_tea(self):
        return 'Вы заказали черный чай'
    
class TeaGreen(AbstractTea):
    def useful_tea(self):
        return 'Вы заказали зеленый чай'
    
class WaterSimple(AbstractWater):
    def useful_water(self):
        return 'Вы заказали простую воду'
    
class WaterMinerale(AbstractWater):
    def useful_water(self):
        return 'Вы заказали минеральную воду'
    
class Calucaled:
    
    def __init__(self, discount, price) -> None:
        self.discount = discount
        self.price = price
    
    def calculated(price, discount):
        return price * discount

class Order:
    def show_result(result_price: Calucaled, drink : AbstractManufacturer, num):
        match num:
            case 1:
                coffee = drink.create_coffee()
                print(coffee.useful_coffee(),'\n','Цена:',result_price)
            case 2:
                tea = drink.create_tea()
                print(tea.useful_tea(),'\n','Цена:',result_price)
            case 3:
                water = drink.create_water()
                print(water.useful_water(),'\n','Цена:',result_price)
            case _:
                print('Неверный ввод!')



if __name__ == '__main__':
    Order.show_result(Calucaled.calculated(10, 1),ConcreteManufacturer1(), 3)
    