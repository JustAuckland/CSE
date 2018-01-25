import random
import string

""""

Outline of Hangman
1. Make a word bank - 10 items
2. Select a random item from the list
3. Add the guessed letter to a list of letters_guessed
4. Reveal the letters if they've been guessed
5. Create the win condition

"""""


guessesLeft = 0
alphabet = list(string.ascii_lowercase)
lettersGuessed = []

bank = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "AuelionSol" "Azir", "Bard",
        "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "ChoGath", "Corki", "Darius", "Diana",
        "DrMundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio",
        "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern",
        "Janna", "JarvanIV", "Jax", "Jayce", "Jinx", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle",
        "Kayne", "Kennen", "KhaZix", "Kindred", "Kled", "KogMaw", "LeBlanc", "LeeSin", "Leona", "Lissandra", "Lucian",
        "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "MasterYi", "MissFortune", "Mordekaiser", "Morgana", "Nami",
        "Nasus", "Nautilus", "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Quinn",
        "Rakan", "Rammus", "RekSai", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sejuani", "Shaco", "Shen",
        "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Syndra", "TahmKench", "Taliyah",
        "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "TwistedFate", "Twitch", "Udyr",
        "Urgot", "Varus", "Vayne", "Veigar", "VelKoz", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong",
        "Xayah", "Yasuo", "Yorick", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]

word = random.choice(bank)
word = word.lower()
print(word)
wordList = list(word)

response = ""
while response != "yes":
        response = input("Are your ready to begin?(Type \"yes\" to continue : ")

blank = '_ ' * len(word)
print("Your Word is : ")
print(blank)

while guessesLeft != 10:
        compare = []
        guess = input("Make a guess")
        for letter in word:
                if letter in lettersGuessed:
                        compare.append(guess)
                        guessesLeft += 1
                else:
                        compare.append("_ ")
        print(compare)
        guess = input("Make a guess")
        lettersGuessed.append(guess)
