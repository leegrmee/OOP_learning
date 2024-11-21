"""
클래스 변수: 클래스 정의에서 메서드 밖에 존재하는 변수
해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수
클래스 변수는 클래스 내외부에서 "클래스명.변수명" 으로 엑세스 가능

인스턴스 변수: 클래스 정의에서 메서드 안에서 사용되면서 "self.변수명"처럼 사용되는 변수
각 객체별로 서로 다른 값을 가짐
클래스 내부에서는 self.인스턴스변수명 을 사용하여 엑세스, 클래스 밖에서는 객체명.인스턴스변수명 으로 엑세스

"""


class Robot:  # 클래스 명

    # 클래스 변수: 인스턴스들이 공유하는 변수
    population = 0

    def __init__(
        self, name, code
    ):  # 생성자 함수/인스턴스가 생성될 때 초기화 시켜주는 함수  / 셀프=각각의 인스턴스
        self.name = (
            name  # 인스턴스 변수/ 각 인스턴스 안의 공간(네임스페이스)에 변수가 저장
        )
        self.code = code  # 인스턴스 변수
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed")

    @classmethod
    def how_many(cls):  # cls =class
        print(f"We have {cls.population} robots.")


print(Robot.population)

siri = Robot("siri", 12345)
print(Robot.population)

jarvis = Robot("jarvis", 12349)
print(Robot.population)

Robot.how_many()
