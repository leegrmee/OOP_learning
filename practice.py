class Circle:
    def __init__(self, name, radius):
        # 생성자에서만 attribute 값 설정 가능
        self.__name = name
        self.__radius = radius

    def name(self):
        return self.__name

    def area(self):
        area = 3.14 * self.__radius**2
        return area

    def length(self):
        length = 2 * 3.14 * self.__radius
        return length


# circle = Circle("circle", 10)
# print(circle.name())
# print(circle.area())
# print(circle.length())

"""
#*캡슐화



class Account:
    def __init__(self):
        self.__amount = 0

    def __withdraw(self, amount):
        if self.__amount < amount:
            print("Insufficient balance")
        else:
            self.__amount -= amount
            return self.__amount

    def __deposit(self, amount):
        self.__amount += amount
        return self.__amount

    def get_amount(self):
        return self.__amount


class Grade:
    def __init__(self, name, korean, english, math):
        self.__name = name
        self.__korean = korean
        self.__english = english
        self.__math = math

    def __get_average(self):
        return (self.__korean + self.__english + self.__math) / 3

    def __get_total(self):
        return self.__korean + self.__english + self.__math


class Pizza:
    def __init__(self, storename: str, menu: list):
        self.__storename = storename
        self.__menu = menu

    def check_menu(self, pizza_name: str):
        if pizza_name in self.__menu:
            return f"Yex, {pizza_name} is available"
        else:
            return "No"


# pizza = Pizza("happy", ["cheese", "pepperoni", "potato"])
# print(pizza.check_menu("cheese"))
"""

""" 
# 다형성/메서드명을 동일하게 해서 같은 모양의 코드가 다른 동작을 하도록 하는 다형성 예
class Elf:
    def __init__(self, name):
        self.name = name

    def attack(self):
        return f"{self.name} 마법 공격"


class Fighter:
    def __init__(self, name):
        self.name = name

    def attack(self):
        return f"{self.name} 주먹 공격"


elf = Elf("hi")
fighter = Fighter("캡틴아메리카")
ourteam = [elf, fighter]
for attacker in ourteam:
    print(attacker.attack())
"""


class Keyword:
    def __init__(self, word):
        self.word = word

    def __len__(self):
        return len(self.word)

    def __getitem__(self, index):
        return self.word[index]

    def get_word(self):
        return self.word


keyword = Keyword("hello")

apple = Keyword("apple")
banana = Keyword("banana")
pineapple = Keyword("pineapple")
grape = Keyword("grape")
orange = Keyword("orange")
lemon = Keyword("lemon")
watermelon = Keyword("watermelon")
melon = Keyword("melon")
gratefruit = Keyword("gratefruit")
strawberry = Keyword("strawberry")

fruits = [
    apple,
    banana,
    pineapple,
    grape,
    orange,
    lemon,
    watermelon,
    melon,
    gratefruit,
    strawberry,
]

# keywords = sorted(fruits, key=lambda x: x.__len__())
# for keyword in keywords:
#     print(keyword.get_word())

# keywords = sorted(fruits, key=lambda x: x[1])
# for keyword in keywords:
#     print(keyword.get_word())

"""
from abc import *


class GameCharacter:
    def __init__(
        self, name="yourname", health=100, striking_power=3, defensive_power=3
    ):
        self.name = name
        self.health = health
        self.striking_power = striking_power
        self.defensive_power = defensive_power

    def info(self):
        return f"name: {self.name}, health: {self.health}, striking_power: {self.striking_power}, defensive_power: {self.defensive_power}"

    @abstractmethod  # 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용/ 추상메소드가 있는 클래스를 상속받으면 반드시 구현해야 함
    def attack(self):
        pass

    @abstractmethod
    def receive_damage(self):
        pass


class Warrior(GameCharacter):
    def attack(self, target):
        print(f"{target.name} attacked with knife")
        target.receive_damage(self.striking_power)

    def receive_damage(self, enemy):
        self.health -= enemy.striking_power
        if self.health <= 0:
            print("Game Over")


class Elf(GameCharacter):
    def attack(self, target):
        print("Attack with magic")
        target.receive_damage(self.striking_power)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Game Over")

    def wear_manteau(self):
        print("Defense attack")
        self.defensive_power += 3


class Wizard(GameCharacter):
    def attack(self, target):
        print("Attack with magic")
        target.receive_damage(self.striking_power)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Game Over")

    def use_wizard(self):
        self.health += 3


warrior = Warrior("warrior", 50, 5, 5)
elf = Elf("elf", 50, 5, 5)
wizard = Wizard("wizard", 50, 5, 5)
"""

from typing_extensions import TypedDict


class User(TypedDict): #TypedDict의 키는 반드시 문자열이어야
    "12" : str
    name: str
    age: int


user: User = {"12": "hello", "name": "hello", "age": 23}
print(user)
