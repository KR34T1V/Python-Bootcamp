import random, sys, locale

nbr_min = 1
nbr_max = 10
if (len(sys.argv) < 1):
	print("Please Guess a number!")
elif (locale.atoi(sys.argv[1]) < nbr_min or locale.atoi(sys.argv[1]) > nbr_max):
	print("You exceeded the boundries. min = %d, max = %d, user = %d" % (nbr_min, nbr_max, locale.atoi(sys.argv[1])))
else:
	user_number = locale.atoi(sys.argv[1])
	number = random.randint(nbr_min, nbr_max)
	if (user_number < number):
		print("You are too low! %d < %d" % (user_number, int(number)))
	elif (user_number > number):
		print("You are too high! %d > %d" % (user_number, int(number)))
	else:
		print("You are correct! %d == %d" % (user_number, int(number)))