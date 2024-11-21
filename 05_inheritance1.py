"""
* [클래스 상속]
추상화(abstraction): 여러 클래스에 중복되는 속성, 메서드를 하나의 기본 클래스로 작성하는 작업
상속(inheritance): 기본 클래스의 공통 기능을 물려받고, 다른 부분만 추가 또는 변경하는 것
이 때 기본 클래스는 부모 클래스(또는 상위 클래스), Parent, Super, Base class 라고 부름
기본 클래스 기능을 물려받는 클래스는 자식 클래스(또는 하위 클래스), Child, Sub, Derived class 라고 부름

* 1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

* 2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.

* 3. 메서드 오버라이딩

* 4. super()

* 5. Python의 모든 클래스는 object 클레스를 상속한다. : 모든 것은 객체이다.

* MyClass.mro() --> 상속 관계를 보여준다.
"""


class Robot:
    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
    """

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."

    @staticmethod
    def are_you_robot():
        print("yes!!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!")
        return f"{self.name} call!!"


class Siri(Robot):
    pass


siri = Siri("iphone8")

print(siri)
siri.are_you_robot()
print(siri.cal_add(17, 19))
