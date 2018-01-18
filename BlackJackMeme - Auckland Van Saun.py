# import sys
# blackjackMeme = True
# while blackjackMeme == True:
# blackjackMeme = False
# sys.exit()

# cardNum = random.randint(1, 13)
# ranSuit = random.randint(1, 4)

# if ranSuit == 1:
#     suit = 'clubs'
# if ranSuit == 2:
#     suit = 'spades'
# if ranSuit == 3:
#     suit = 'diamonds'
# if ranSuit == 4:
#     suit = 'hearts'

import random
gameMeme = True

ranSuit = 0
ranSuit2 = 0
suit = 0
suit2 = 0
#gameMeme = 0

dealerName = random.randint(1, 6)

if dealerName == 1:
    dealerName = "Lucas"
if dealerName == 2:
    dealerName = "Dan"
if dealerName == 3:
    dealerName = "Bob"
if dealerName == 4:
    dealerName = "Sydney"
if dealerName == 5:
    dealerName = "Aubrey"
if dealerName == 6:
    dealerName = "Ruby"



if gameMeme == True:
    print('  Hi!\n  My name is Dealer %s' % dealerName )
    name = input('  What\'s yours')
    print('  Nice to meet you %s!' % name)
    print('  Alright lets get started shall we!')

    cardNum = random.randint(1, 13)
    cardNum2 = random.randint(1, 13)
    ranSuit = random.randint(1, 4)
    ranSuit2 = random.randint(1, 4)

    if ranSuit == 1:
        suit = 'clubs'
    if ranSuit == 2:
        suit = 'spades'
    if ranSuit == 3:
        suit = 'diamonds'
    if ranSuit == 4:
        suit = 'hearts'

    if ranSuit2 == 1:
        suit2 = 'clubs'
    if ranSuit2 == 2:
        suit2 = 'spades'
    if ranSuit2 == 3:
        suit2 = 'diamonds'
    if ranSuit2 == 4:
        suit2 = 'hearts'


