

class Calculator:
	def __init__(self, first_value=0):  # 기본값 지정. 객체 생성 시 first_value을 안 써주면 기본값 0
		self.value = first_value

	def add(self, a):
		self.value += a

	def sub(self, a):
		self.value -= a

	def reset(self):
		self.value = 0

if __name__=='__main__':	
	# import 당할때는 실행x
	# python calc_basic.py 로 직접 실행 할 때만 돌아가는 코드

	c1 = Calculator(100)  # => __init__ 메소드의 첫번째인자인 first_value에 100이 들어감

	c1.add(100)
	print(c1.value)
	c1.sub(20)
	print(c1.value)

	c1.reset()
	print(c1.value)

	c2 = Calculator()  # first_value를 입력 안 해주면 기본값인 0으로 들어감

	print(c2.value)


