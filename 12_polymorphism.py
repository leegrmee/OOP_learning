"""
#* polymorphism
#* 여러 형태를 가질 수 있도록 한다. 즉, 객체를 부품화할 수 있도록 한다.
#* 같은 형태의 코드가 다른 동작을 하도록 하는 것


같은 모양의 코드가 다른 동작을 하는 것
키보드의 예로
push(keyboard): 키보드를 누룬다는 동일한 코드에 대해
ENTER, ESC, A 등 실제 키에 따라 동작이 다른 것을 의미함
다형성은 코드의 양을 줄이고, 여러 객체 타입을 하나의 타입으로 관리가 가능하여 유지보수에 좋음

Method Override (메서드 재정의) 도 다형성의 한 예
메서드명을 동일하게 해서 같은 모양의 코드가 다른 동작을 하도록 하는 다형성 예
"""


class Robot:
    """
    Robot Class
    """

    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1

    @property
    def name(self):
        return f"yoon {self.__name}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age - self.__age == 1:
            self.__age = new_age
        else:
            raise ValueError()

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.__name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.__population} robots."


class Siri(Robot):
    def say_apple(self):
        print("hello my apple")


class SiriKo(Robot):
    def say_apple(self):
        print("안녕하세요")


class Bixby(Robot):
    def say_samsung(self):
        print("안녕하세요ㅕ")
