import random

numBank = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
suitBank = ["hearts", "clubs", "diamonds", "spades"]

for word in numBank:
    ace = 11
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 10
    queen = 10
    king = 10

ranNumP = random.choice(numBank)
ranSuitP = random.choice(suitBank)
ranNumP2 = random.choice(numBank)
ranSuitP2 = random.choice(suitBank)
ranNumD = random.choice(numBank)
ranSuitD = random.choice(suitBank)
ranNumD2 = random.choice(numBank)
ranSuitD2 = random.choice(suitBank)

playerCard1 = ("%s of %s" % (ranNumP, ranSuitP))
playerCard2 = ("%s of %s" % (ranNumP2, ranSuitP2))
dealerCard1 = ("%s of %s" % (ranNumD, ranSuitD))
dealerCard2 = ("%s of %s" % (ranNumD2, ranSuitD2))

playerHand = (playerCard1, playerCard2)
dealerHand = (dealerCard1, dealerCard2)

bank = 25

input("(Type anything to begin) : ")

print("Hi I'm dealer Sarah!\nReady to play?")
while bank != 0:
    bet = input("Place your bet (you have %i dollars in your bank)" % bank)
    if bet not in '0123456789':
        print("Please only guess numbers!")

    bank = bank - (int(bet))

