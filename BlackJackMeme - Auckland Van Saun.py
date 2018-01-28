import random

numBank = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
suitBank = ["hearts", "clubs", "diamonds", "spades"]

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
while bank != 0:
    print("Hi I'm dealer Sarah!\nReady to play?")
    bet = input("Place your bet (you have %s dollars in your bank)" % bank)
    bank = bank -
    print(bank)

