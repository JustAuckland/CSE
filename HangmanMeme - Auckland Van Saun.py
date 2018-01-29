import random

guessesLeft = 0
lettersGuessed = []

bank = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "AurelionSol", "Azir", "Bard",
        "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "ChoGath", "Corki", "Darius", "Diana",
        "DrMundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio",
        "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern",
        "Janna", "JarvanIV", "Jax", "Jayce", "Jinx", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle",
        "Kayn", "Kennen", "KhaZix", "Kindred", "Kled", "KogMaw", "LeBlanc", "LeeSin", "Leona", "Lissandra", "Lucian",
        "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "MasterYi", "MissFortune", "Mordekaiser", "Morgana", "Nami",
        "Nasus", "Nautilus", "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Quinn",
        "Rakan", "Rammus", "RekSai", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sejuani", "Shaco", "Shen",
        "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Syndra", "TahmKench", "Taliyah",
        "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "TwistedFate", "Twitch", "Udyr",
        "Urgot", "Varus", "Vayne", "Veigar", "VelKoz", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong",
        "Xayah", "Yasuo", "Yorick", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]

word = random.choice(bank)
word = word.lower()

wordList = list(word)
guess = []


response = input("Type anyhting to begin : ")

while guessesLeft != 10:
        output = []

        for letter in word:
                if letter in lettersGuessed:
                        output.append(letter)

                else:
                        output.append("_ ")
        if output == wordList:
                print(word)
                print("Good job you're an exper!")
                exit(0)

        oKKo = "".join(output)
        print(oKKo)
        guessesLeft += 1

        guess = input("Make a guess : ")
        if len(guess) != 1:
                print("Please guess one letter at a time!")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                print("Please only guess letters!")
        for letter in output:
                if guess == letter in output:
                        print("You've already guessed this letter")
                        guessesLeft -= 1

        lettersGuessed.append(guess)

print("Ripperoni Pepperoni \nBetter luck next time!")
