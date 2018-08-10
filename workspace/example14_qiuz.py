"""
 
 연습문제 풀이

 """
# 비트 연산
print(4>>2)
print(4<<2)

print()

# 진법 연산
print(0b1001)
print(0xFF)
print(0xF0|0xF0)

#출력 포멧 연습
a = '{0} {1}'.format('Mario',40)
print(a)
b ='{name} {age}'.format(name='KKK',age=25)
print(b)


# * 찍기 1
for i in range(1,6,1):
	for j in range(0,i,1):
		print("*", end="")
	print()
print("\n\n")

# * 찍기 2
for i in range(6,0,-1):
	for j in range(0,i,1):
		print("*", end="")
	print()
print("\n\n")

# * 찍기 3
cnt=0;

while cnt<5:
	cnt = cnt+1
	for j in range(0,cnt,1):
		print("*", end="")
	print()
print("\n\n")

# * 찍기 4
cnt2=6;
while cnt >= 0:
	cnt = cnt-1
	for k in range(0,cnt,1):
		print("*", end="")
	print()
print("\n\n")

# * 찍기 5
num = int(input("반복횟수를 입력하세요 : "))
while num <0:
	print("0보다 작거나 같은 수는 입력할 수 없습니다.")
	num = int(input("반복횟수를 입력하세요 : "))

for i in range(1,num+1,1):
	for j in range(0,i,1):
		print("*", end="")
	print()
print("\n\n")
