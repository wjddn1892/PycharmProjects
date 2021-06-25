# 입금, 출금

class Customer:
	def __init__(self, name, money=0):
		self.money = money  # 현재 잔고

	def deposit(self, amount):

		self.money += amount
		print("현재 잔고는 {}원입니다.".format(self.money))

	def withdraw(self, amount):
		if self.money < amount:
			print("잔고가 부족합니다.")
		else:
			self.money -= amount
		print("현재 잔고는 {}원입니다.".format(self.money))
		

c0 = Customer('changmin')
c1 = Customer('sungjun', 10000)
c2 = Customer('jeongwoo', money=20000)  # 세가지 방법 모두 맞는 방법

# c3 = Customer(money=20000)  => 에러. 필수 입력인 name에 해당하는 인자가 없음

c0.deposit(5000)
c0.withdraw(10000)
print(c1.money)




