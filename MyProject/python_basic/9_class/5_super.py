class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()    # 이 경우에는 처음 상속받음 클래스만 실행됨
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()