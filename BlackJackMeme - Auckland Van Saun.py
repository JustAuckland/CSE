import random

cardNum = random.randint(1,13)
suitNum = random.randint(1,4)

if suitNum == 1:
    suit = 'clubs'
if suitNum == 2:
    suit = 'spades'
if suitNum == 3:
    suit = 'diamonds'
if suitNum == 4:
    suit = 'hearts'

print('  Hi!\n  My name is Dealer Lucas')
name = input('  What\'s yours')
print('  Nice to meet you %s!' % name)
print('  Alright lets get started shall we!')

