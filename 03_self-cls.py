"""
static method: 객체와 독립적이지만, 로직상 클래스내에 포함되는 메서드
self 파라미터를 갖고 있지 않음
객체 속성에 접근 불가
정적 메서드는 메서드 앞에 @staticmethod 라는 Decorator를 넣어야 함
클래스명.정적메서드명 또는 객체명.정적메서드명 둘 다 호출 가능

class method: 해당 class 안에서 호출 (해당 클래스로 만들어진 객체에서 호출되지 않고, 직접 클래스 자체에서 호출)
self 파라미터 대신, cls 파라미터를 가짐
클래스 변수 접근 가능하며 cls.클래스변수명 으로 엑세스 가능 단, 객체 속성/메서드는 접근 불가
클래스 메서드는 메서드 앞에 @classmethod 라는 Decorator를 넣어야 함
클래스명.클래스메서드명 또는 객체명.클래스메서드명 둘 다 호출 가능

id(객체명): 객체가 가리키는 실제 주소값

** is 와 == 연산자 차이**

is : 가리키는 객체 자체가 같은 경우 True
== : 가리키는 값들이 같은 경우 True
"""


class SelfTest:
    name = "kate"

    def __init__(self, x):
        self.x = x

    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")

    def func2(self):
        print(f"self: {self}")
        print("class 안의 self 주소", id(self))
        print("func2")


test_obj = SelfTest(10)

test_obj.func2()  # class 안의 self 주소 4379983776
SelfTest.func1()  # cls: <class '__main__.SelfTest'> 클래스 그 자체

print("인스턴스 주소", id(test_obj))  # 인스턴스 주소 4379983776

test_obj2 = SelfTest(20)
test_obj2.func2()
print("인스턴스 주소", id(test_obj))

test_obj.func1()
# 이렇게 작성해도 파이썬이 스스로 클래스 네임스페이스에 접근함.
# 파이썬의 동적 타이핑 덕분에 이런 일이 가능함.
print(test_obj.name)  # 이것도 같은 원리로 가능
