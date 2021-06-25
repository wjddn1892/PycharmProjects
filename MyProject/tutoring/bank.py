class Customer:
    all_customers = [] # 객체의 변수x, 클래스 변수 => all_customer 앞에 Customer.을 붙여줘야함
    
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
        customer = Customer.all_customers[id]
        print('예금주: {}'.format(customer.name))
        
        answer = input('예금주: {} 맞습니까? y/n'.format(customer.name))
        if answer == 'y':
            customer.money += amount
            self.money -= amount
            print('현재 잔고는 {}원입니다.'.format(self.money))

        else:
            print('취소되었습니다.')
        
        
        


c0 = Customer('cm') # all_customers = [c0]
c1 = Customer('sj', 10000) # all_customers = [c0, c1]

c0.send(1, 1000)

print(len(all_customers))

print(c0.id)
print(c1.id)
