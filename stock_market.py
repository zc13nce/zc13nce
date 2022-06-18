# Stock market game with 365 days of trading.

from os import system
from random import choice, randint
from threading import Thread
from time import sleep


def clear():
	system('clear')


def n(t):
	return "{:,}".format(t)


def loadingText():
	sleep(5)
	if isLoading: print('Still loading...')
	sleep(6)
	if isLoading:
		print('This isn\'t annoyingly long fake loading, don\'t worry...')
	sleep(7)
	if isLoading: print('Alllllmost done...')
	sleep(15)
	if isLoading: print('Well, it should\'ve loaded so uh... refresh?')


loader = Thread(target=loadingText)

try:
	exec('from getkey import getkey')
except:
	isLoading = True
	loader.start()
	print(
	    '~~~~~~~~~~~~~~~~~\n|  S T O N K S  |\n~~~~~~~~~~~~~~~~~\n\nInitializing businessman mode...'
	)
	system('pip install getkey -q -q -q')
	isLoading = False
	exec('from getkey import getkey')
	clear()

print('~~~~~~~~~~~~~~~~~\n|  S T O N K S  |\n~~~~~~~~~~~~~~~~~')
print()
print('Objective: Buy low and sell high until you\'re the richest in town :)')
print()
print('Any key to start.')
getkey()

clear()

day = 0
money = 1000
stocks = ['MRV', 'CAT', 'MSA', 'CHKN', 'SPC', 'PY', 'RPLT', 'HI', 'AMGS']
wordList = [
    'banking', 'stocks', 'saving', 'money', 'finance', 'vault', 'credit',
    'debt', 'loan', 'deposit', 'withdraw', 'rich', 'dollar', 'coin', 'barter',
    'trade', 'scam', 'millionare', 'billionare', 'trillionare', 'broker',
    'jackpot', 'bankruptcy', 'market', 'industry', 'revenue', 'adertisement',
    'cheap', 'expensive', 'invest'
]
keyIndicator = [['A', 'B', 'C', 'D', 'E'], [1, 2, 3, 4, 5]]

displayedStocks = []
for i in range(5):
	displayedStocks.append(stocks.pop(randint(0, len(stocks) - 1)))
stocks = {}

for i in displayedStocks:
	stocks[i] = {'price': randint(10, 700), 'owned': 0}

while day < 365:
	day += 1
	print('~~~~~~~~~~~~~~~~~\n|  S T O N K S  |\n~~~~~~~~~~~~~~~~~\n')
	print(f'Day: {day}/365{" "*(8-len(str(day)))}Money: ${n(money)}')
	print('Word of the day:', choice(wordList))

	print('\nToday\'s stocks:                buy  sell')
	inc = -1
	for i in stocks:
		inc += 1
		stockStr = f'{i}: ${n(stocks[i]["price"])} ({n(stocks[i]["owned"])} owned)'
		stockLen = len(stockStr)

		print(
		    f'{stockStr}{" "*(32-stockLen)}{keyIndicator[0][inc]}    {keyIndicator[1][inc]}'
		)

	print('\nSkip day                        F')
	print('\nType the letter of what action you want to do')
	while True:
		key = getkey().lower()
		if key in 'abcde':
			currentStock = displayedStocks[keyIndicator[0].index(key.upper())]
			clear()
			print('~~~~~~~~~~~~~~~~~\n|  S T O N K S  |\n~~~~~~~~~~~~~~~~~\n')
			print(
			    f'Buying {currentStock}.\nYou can buy up to {n(money//stocks[currentStock]["price"])}.\n'
			)
			print('Buy all       A\nBuy some      B\nCancel        C')
			while True:
				key = getkey().lower()
				if key == 'a':
					stocks[currentStock][
					    'owned'] += money // stocks[currentStock]["price"]
					money = money % stocks[currentStock]['price']
					break

				elif key == 'b':
					while True:
						print('\nHow many do you want to buy?')
						buyNum = input('> ')
						try:
							buyNum = int(buyNum)
							if buyNum < 0: e = int('beans')
							break
						except:
							print('That\'s not a number :/\n')
					if money // stocks[currentStock]["price"] < buyNum:
						print(
						    'You either can\'t read or are trying to cheat, you lose a day.'
						)
					else:
						money -= stocks[currentStock]['price'] * buyNum
						stocks[currentStock]['owned'] += buyNum
					print('\nAny key to continue.')
					getkey()
					break

				elif key == 'c':
					break
			break
		elif key in '12345':
			clear()
			currentStock = displayedStocks[keyIndicator[1].index(int(key))]
			print('~~~~~~~~~~~~~~~~~\n|  S T O N K S  |\n~~~~~~~~~~~~~~~~~\n')
			print(
			    f'Selling {currentStock}.\nYou own {n(stocks[currentStock]["owned"])}.\n'
			)

			print('Sell all      A\nSell some     B\nCancel        C')

			while True:
				key = getkey().lower()
				if key == 'a':
					money += stocks[currentStock]['owned'] * stocks[
					    currentStock]['price']
					stocks[currentStock]['owned'] = 0
					break
				if key == 'b':
					while True:
						print('\nHow many do you want to sell?')
						sellNum = input('> ')
						try:
							sellNum = int(sellNum)
							if sellNum < 0: e = int('beans')
							break
						except:
							print('That\'s not a number :/\n')
					if stocks[currentStock]["owned"] < sellNum:
						print(
						    'You either can\'t read or are trying to cheat, you lose a day.'
						)
					else:
						money += stocks[currentStock]['price'] * sellNum
						stocks[currentStock]['owned'] -= sellNum
					print('\nAny key to continue.')
					getkey()
					break
				if key == 'c':
					break

			break

		elif key == 'f':
			break

	for i in stocks:
		stocks[i]['price'] += randint(-200, 200)
		if stocks[i]['price'] < 1:
			stocks[i]['price'] = randint(1, 30)

	clear()

print('~~~~~~~~~~~~~~~~~\n|  S T O N K S  |\n~~~~~~~~~~~~~~~~~\n')
print('You finished the year!\n')

print(f'Ending money: ${n(money)}')

for i in stocks:
	money += stocks[i]['owned'] * stocks[i]['price']

print(f'Money with shares sold: ${n(money)}')
