import random

""""

Outline of Hangman
1. Make a word bank - 10 items
2. Select a random item from the list
3. Hide the word (use *)
4. Reveal the letters if they've been guessed
5. Create the win condition

"""""

bank = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu","Anivia", "Annie", "Ashe", "Azir", "Blitzcrank", "Brand", "Braum",
"Caitlyn", "Cassiopeia", "ChoGath", "Corki", "Darius", "Diana", "DrMundo", "Draven", "Elise", "Evelynn", "Ezreal",
"Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Hecarim", "Heimerdinger", "Irelia",
"Janna", "JarvanIV", "Jax", "Jayce", "Jinx", "Kalista", "Karma", "Karthus",
KassadinKatarinaKayleKayneKennenKhaZixKogMawLeBlancLeeSinLeonaLissandraLucianLuluLuxMalphiteMalzaharMaokaiMasterYi
Miss FortuneMordekaiserMorganaNamiNasusNautilusNidaleeNocturneNunuOlafOriannaOrnPantheonPoppyQuinnRammusRekSaiRenekton
RengarRivenRumbleRyzeSejuaniShacoShenShyvanaSingedSionSivirSkarnerSonaSorakaSwainSyndraTalonTaricTeemoThreshTristana
YasuoYorickZacZedZiggsZileanZoeZyra
word = random.randint(0,134)
print(bank[word])


