class calculator:
    def __init__(self):    # init은 생성자 필수로 들어가야함
        self.value = 0

    def add(self, a):
        self.value += a

c = calculator()
print(c.value)

c.add(10)
print(c.value)

c.add(15)
print(c.value)


__init__(self, a, b = 0)   # 초기값이 정해진 경우는 맨 뒤에 표기 (b가 0으로 초기값 정해짐) 

--------------------------

class calculator:
    def __init__(self):
        self.value = 0

    def sub(self, a, b):
        c = a - b
        self.value = c

    def reset(self):
        self.value = 0

c = calculator()
print(c.value)

c.sub(100, 555)
print(c.value)

c.reset()
print(c.value)

--------------------------------

from exc import calculator # 다른 파일에서 exc파일을 불러오는 역할

c = calculator()

c.add(10, 5)
print(c.value)

-----------------------------

class calculator:
    def __init__(self):
        self.value = 0

    def add(self, a, b):
        c = a + b
        self.value = c

    def sub(self, a, b):
        c = a - b
        self.value = c

    def reset(self):
        self.value = 0

if __name__ == '__main__': # import 당할 때는 밑에 있는 것들이 실행x  직접 자기 파일 안에서 실행할 때만 돌아가는 코드

c = calculator()
print(c.value)

c.sub(100, 555)
print(c.value)

c.reset()
print(c.value)

------------------------

#통장 잔고 출력#

class customer:
    def __init__(self):
        self.money = 0

    def deposit(self, amount):
        self.money += amount
        print('현재 잔고는 {}원 입니다.'.format(self.money))

    def withdraw(self, amount):
        self.money -= amount
        
        if self.money < 0:
            print('현재 잔고가 부족합니다.')
            
        else:
            print('현재 잔고는 {}원 입니다.'.format(self.money))

c = customer()

c.deposit(10000)

c.withdraw(50000)

------------------------------

class Customer:
    all_customers = [] # 객체의 변수x, 클래스 변수 => all_customer 앞에 customer.을 붙여줘야함
    
    def __init__(self, name, money = 0):
        self.money = money
        self.name = name
        self.id =len(all_customers)
        Customer.all_customers.append(self)

    def deposit(self, amount):
        self.money += amount
        print('현재 잔고는 {}원 입니다.'.format(self.money))

    def withdraw(self, amount):
        self.money -= amount
        
        if self.money < 0:
            print('현재 잔고가 부족합니다.')
            
        else:
            print('현재 잔고는 {}원 입니다.'.format(self.money))
            
    def send(self, id, amount):
        customer = Customer.all_customer[id]
        print('예금주: {}'.format(customer.name))

        customer.money += amount
        self.money -= amount


c0 = customer('cm') # all_customers = [c0]
c1 = customer('sj', 10000) # all_customers = [c0, c1]

c0.send(1, 1000)

print(len(all_customers))

print(c0.id)
print(c1.id)

