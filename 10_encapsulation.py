"""
* public vs private

private -> protected -> public
private: private로 선언된 attribute, method는 해당 클래스에서만 접근 가능
protected: protected로 선언된 attribute, method는 해당 클래스 또는 해당 클래스를 상속받은 클래스에서만 접근 가능
public: public으로 선언된 attribute, method는 어떤 클래스라도 접근 가능

"""


class Robot:
    """
    Robot Class
    """

    population = 0

    def __init__(self, name, age):
        self.name = name
        self._age = age
        Robot.population += 1

    def __say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(self.name)
        print(self._age)


ss = Robot("yss", 8)


ssss = Siri("iphone8", 9)

print(ssss)
