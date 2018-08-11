"""
	생성자 상속
	//super()
"""

class Animal:
	def __init__(self,name):
		self.name = name
	def walk(self):
		print("걷는다")
	def eat(self):
		print("먹는다")
	def greet(self):
		print("{}이가 인사한다.".format(self.name))

#생성자는 반드시 상속 받아야한다.
class Human(Animal):
	def __init__(self,name,hand):
		super().__init__(name)
		self.hand = hand
	def wave(self):
		print("{} 손을 흔들면서".format(self.hand))
	def disp(self):
		self.wave() # 자기자신
		super().greet() #부모

human = Human("사람", "오른손")
human.disp()
