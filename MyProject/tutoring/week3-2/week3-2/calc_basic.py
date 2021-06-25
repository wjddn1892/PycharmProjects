'''

게임 캐릭터를 구현하려고 할 때
캐릭터의 속성(hp, 직업, 아이템 등)을 모두 변수로 구현할 수 없다.

ch1_hp = 100
ch1_job = "마법사"
ch1_item1 = "물약"

ch2_hp = 90
ch1_job = "학생"

... 너무 비효율적

=> Character라는 클래스(틀)를 만들고 여러 캐릭터들을 찍어낸다(객체 생성)
클래스와 객체 참고
https://wikidocs.net/28#_2


ch1 = Character()
ch2 = Character()
...


'''


# 클래스: 변수와 함수의 묶음
# 클래스 내부에서 쓰이는 함수를 method라고 한다.
# method의 첫번째 매개변수는 항상 self
class Calculator:
	def __init__(self):
		self.value = 0
	# 객체가 생성될 때 자동으로 실행되는 내장 method.
	# 객체가 가지고 있는 변수를 초기화(정의)해줌

	def add(self, a):

		self.value += a  # => self.value = self.value + a 와 같은 뜻

	def sub(self, a):
		self.value -= a

	def reset(self):
		self.value = 0


c = Calculator()  # c라는 객체 생성. Calculator라는 틀(클래스)로 찍어낸 하나의 붕어빵
print(c.value)
c.add(100)
# 실제로 쓸 때는 클래스의 add(self, a)에서 self는 넘어가고 a 자리에 100이 들어간다.

print(c.value)  # 클래스에서 self.value로 정의한 변수는 객체.value로 확인할 수 있다
c.sub(20)
print(c.value)

c.reset()
print(c.value)

