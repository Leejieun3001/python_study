# 함수문제

#평균 구하기
def average(*num):
	result = 0
	for s in num:
		result = result + s
	avg = result / len(num)
	print(avg)
	
average(1,2,3,4,5)

print("\n\n")
# * 출력하기
def print_start(num):
	for i in range (num,0,-1):
		for j in range (i):
			print("*", end="")
		print()

print_start(5)

# 클래스 문제