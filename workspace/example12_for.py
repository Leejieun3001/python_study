"""
  for문 제어 연습
  
  for 변수 in range (start, end, step):
	 수행할 문장
 
"""

#for 문
for i in range(0,5,1): #start, end, step
	print(i,end = "    ")
print()

for i in range(10, 0, -1):
	print(i, end ="\t")
print()

for i in range(0,5): #step 생략시 1씩 증가
	print(i, end ="\t")
print()


for i in range(5): #start 생략시 0부터 시작 step 생략시 1씩 증가
	print(i, end ="\t")
print()

# 다중 for문
for i in range(1,6):
	for j in range(i):
		print("*",end ="")
	print()
print()


for i in range(5,0,-1):
	for j in range(i):
		print("*",end ="")
	print()
print()


#break
for i in range(10):
	if i==5:
		break
	print(i, end="\t")
print()

#continue
for i in range(10):
	if i==5:
		continue
	print(i, end="\t")
print()

	



