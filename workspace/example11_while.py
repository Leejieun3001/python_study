"""
  while문 제어 연습
  
  while 조건:
 
"""
#while 문 1
limit = int(input("몇번 반복 할까요 ?"))

count = 0
while count < limit:
	count = count + 1
	print("{}회 반복 합니다.".format(count))
	
print("count 반복문 종료합니다. \n\n")


#while 문 2

treeHit =0
while treeHit < 10:
	treeHit = treeHit + 1
	print("나무를 {}번 찍었습니다.".format(treeHit))
	
	if treeHit ==10:
	  print("나무가 넘어갑니다.")
print("treeHit 종료합니다.") 


#while 문 3

while True:
	print("반복을 계속할까요 ? [예/아니오]:")
	answer = input()
	
	if answer == "예" or answer =="y" :
		print("반복을 계속합니다.")
	elif answer == "아니오" or answer == "n":
		 break
	else:
		print("정상적인 답변을 입력해 주세여")
	