

class Customer:
	all_customers = []  # 객체의 변수 x, 클래스 변수  => Customer.all_customers로 쓸 수 있음.

	def __init__(self, name, money=0):
		self.money = money
		self.name = name
		self.id = len(Customer.all_customers)  # 객체의 아이디 지정해주기. Customer.all_customers의 원소 개수를 객체의 고유 id로 만들어줌
		Customer.all_customers.append(self)  # 생성된 객체(변수와 메소드 묶음 전체)가 Customer.all_customers에 순서대로 쌓임.
											# 이 때 len(Customer.all_customers)는 1만큼 증가
	def deposit(self, amount):

		self.money += amount
		print("현재 잔고는 {}원입니다.".format(self.money))

	def withdraw(self, amount):
		if self.money < amount:
			print("잔고가 부족합니다.")
		else:
			self.money -= amount
			print("현재 잔고는 {}원입니다.".format(self.money))

	def send(self, customer_id, amount):
		customer = Customer.all_customers[customer_id]  # => 송금하고 싶은 customer 객체

		answer = input("예금주: {} 맞습니까? y/n".format(customer.name))

		if answer == 'y':
			customer.money += amount
			self.money -= amount
			print("현재 잔고는 {}원입니다.".format(self.money))
			
		else:
			print("취소되었습니다")


c0 = Customer('changmin')
c1 = Customer('sungjun', 10000)
c2 = Customer('jeongwoo')

c0.send(1, 1000)

