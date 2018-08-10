#복잡한 if문 {}이 없기 때문에 들여쓰기를 주의해야 한다

if True:
	print("블럭에 속한 코드")
	print("여러줄 블럭은")
	print("블럭을 맞춰야 한다.")
	print("블럭에 끝은 내여쓰기")
print("블럭이 끝났음 \n")


if False:
	print("블럭에 속한 코드")
	print("여러줄 블럭은")
	print("블럭을 맞춰야 한다.")
	print("블럭에 끝은 내여쓰기")
print("블럭이 끝났음 \n")


if True:
	print("블럭에 속한 코드")
	
	if False:
		print("apple")
	if True:
		print("banana")
		


if True:
	print("블록에 속한 코드")
	
	if False:
		print("apple")
	if True:
		print("banana")
		
		if True:
			print("banana is delicious")
		
		print("OK")

	print("블럭에 끝은 내여쓰기")
print("블럭이 끝났음 \n")
