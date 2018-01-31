
import random
import string


def game():
        
        guesses_left = 10
        letters_guessed = list(string.punctuation + " ")

        bank = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "Aurelion Sol", "Azir", 
                "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", 
                "Darius", "Diana", "Dr.Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", 
                "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", 
                "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jinx", "Kalista", "Karma", "Karthus", 
                "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "LeBlanc", 
                "Lee Sin", "Leona", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi",
                "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Nidalee", "Nocturne", "Nunu", 
                "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Renekton", 
                "Rengar", "Riven", "Rumble", "Ryze", "Sejuani", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", 
                "Skarner", "Sona", "Soraka", "Swain", "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", 
                "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", 
                "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", 
                "Xin Zhao", "Yasuo", "Yorick", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]

        word = random.choice(bank)

        word_list = list(word)
        # response = input("Type anything to begin : ")
        output = []
        while guesses_left > 0:
                output = []

                for letter in word:
                        if letter.lower() in letters_guessed:
                                output.append(letter)
                        else:
                                output.append("_")

                if output == word_list:
                        print(word)
                        print("Good job you're an exper!")
                        exit(0)

                join = " ".join(output)
                print(join)
                print(guesses_left)
                guess = input("Make a guess : ").lower()

                if guess.lower() in word.lower():
                        guesses_left -= 1
                else:
                        guesses_left += 0

                if len(guess) != 1:
                        print("Please guess one letter at a time!")
                elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                        print("Please only guess letters!")

                letters_guessed.append(guess)

        if output != word_list:
                print("Ripperoni Pepperoni\n your word was %s" % word)
                end = input("Your word was %s\nPress \"yes\" to restart and \"no\" to exit" % word)
                if end.lower() == "no" or "n":
                        exit(0)
                elif end.lower() != "yes" or "y":
                        "please guess \"Yes\" or \"No\""
                else:
                        game()

        else:
                end1 = input("Your word was %s\nPress \"yes\" to restart and \"no\" to exit" % word)
                if end1.lower() == "no" or "n":
                        exit(0)
                elif end1.lower() != "yes" or "y":
                        "please guess \"Yes\" or \"No\""
                else:
                        game()
        print("Ripperoni Pepperoni\n your word was %s" % word)
