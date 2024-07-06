from pyperclip import copy

def getExp():
	exp = int(input("Введи свой текущий Experience: "))
	print()
	return exp

def calcProcent(needed, current, accuracy):
	if accuracy >= 0:
		return int(current / needed * 10**(accuracy+2)) / 10**accuracy
	else:
		raise Exception("Accuracy can't be less zero.")

def roundUp(number):
	decimal = number - int(number)
	if decimal != 0:
		return int(number) + 1
	else:
		return int(number)

def outData(exp):
	expNeeded = 340125
	leftExp = expNeeded - exp
	procentExp = calcProcent(expNeeded, exp, 2)

	print(f"Осталось: {leftExp} exp")
	print(f"Текущий процент: {procentExp}%")
	print(f"Осталось слабой смолы: {roundUp(leftExp / 300)} штук")
	print(f"Осталось первородной смолы: {roundUp(leftExp / 5)} единиц")
	print()
	print(f"Осталось ~дней: {calcProcent(1500 + 800, leftExp, 0) / 100}")

	copy(f"[RU|EN] 60AR первого января. {procentExp}%")


if __name__ == '__main__':
	# outData(308139)
	outData(getExp())
	input()