import random
x=random.randint(1,10)
a=0
while (a!=x):
	a=int(input("Guess the number: "))
	if (a==x):
		print("Correct!")
	else:
		print("Wrong, try again!")

