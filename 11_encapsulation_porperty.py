"""
#* [property]
#* 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
#* 인스턴스 변수 값에 대한 유효성 검사 및 수정
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
    def access_to_name(self):
        return f"yoon {self.__name}"

    @property
    def access_to_age(self):
        if self.__age < 0:
            raise ValueError("age can't be negative")
        return self.__age

    @access_to_age.setter
    def new_age(self, new_age):
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


droid = Robot("Hello", -10)


print(droid.access_to_age)
