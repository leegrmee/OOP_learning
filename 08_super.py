"""
* [클래스 상속]

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
        print(f"{Robot.population} num!")
        print("yes!!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!")
        return f"{self.name} call!!"


class Siri(Robot):
    def __init__(self, name, age):
        # self.name = name
        # self.age = age
        # Siri.population += 1

        super().__init__(name)
        self.age = age

    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        return a * b

    def cal_test(self, a, b):
        super().say_hi()  # Greetings, my masters call me iphone8.
        self.say_hi()  # Greetings, my masters call me iphone8. by apple.
        return self.cal_add(a, b) + self.cal_mul(a, b)

    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple!!")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}. by apple.")

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots. by apple"


# siri = Siri("iphone8", 17)

# siri.say_hi()
# print(Siri.how_many())
siri = Siri("iphone8", 17)
print(siri.name)
print(siri.age)

print(siri.cal_test(1, 3))


"""
Python 2:

class A:
    def __init__(self):
        ...

class B(A):
    def __init__(self):
        super(B, self).__init__()
"""
