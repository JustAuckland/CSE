
import random
import string

# def script():

guessesLeft = 10
lettersGuessed = list(string.punctuation + " ")

bank = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "Aurelion Sol", "Azir", "Bard",
        "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Diana",
        "Dr.Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio",
        "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern",
        "Janna", "Jarvan IV", "Jax", "Jayce", "Jinx", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle",
        "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lissandra", "Lucian",
        "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami",
        "Nasus", "Nautilus", "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Quinn",
        "Rakan", "Rammus", "Rek'Sai", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sejuani", "Shaco", "Shen",
        "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Syndra", "Tahm Kench", "Taliyah",
        "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr",
        "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong",
        "Xayah", "Xin Zhao", "Yasuo", "Yorick", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]

word = random.choice(bank)

wordList = list(word)
guess = []
guess1 = ()
# response = input("Type anything to begin : ")


while guessesLeft > 0:
        output = []

        for letter in word:
                if letter.lower() in lettersGuessed:
                        output.append(letter)
                else:
                        output.append("_")

        if output == wordList:
                print(word)
                print("Good job you're an exper!")
                exit(0)

        join = " ".join(output)
        print(join)
        print(guessesLeft)
        guess = input("Make a guess : ").lower()

        if guess1 != word:
                guessesLeft -= 1

        if len(guess) != 1:
                print("Please guess one letter at a time!")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print("Please only guess letters!")

        lettersGuessed.append(guess) and guess1

# if output != wordList:
#         print("Ripperoni Pepperoni \nBetter luck next time!")
# else:
#         end = input("Your word was %s\nPress anything to restart" % word)
#         if end.lower() == "no" or "n":
#                 exit(0)
#         elif end.lower() != "yes" or "y":
#                 "please guess \"Yes\" or \"No\""
#         else:
#                 test = 0
print("Ripperoni Pepperoni\n your word was %s" % word)

# script()
