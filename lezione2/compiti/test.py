u1 = {
    "nickname": "enkk",
    "gender": "F",
    "games": ["slots", "blackjack"]
}

u2 = {
    "nickname": "Giulia",
    "gender": "F",
    "games": ["roulette", "blackjack"]
}

u3 = {
    "nickname": "Shin",
    "gender": "F",
    "games": ["crazy time", "blackjack"]
}

users = [u1, u2, u3]

# creare una struttura dati che contenga il numero di preferenze associato ad ogni giocoù
games_pref = {}

for user in users:
    for game in user["games"]:
        if game in games_pref.keys():
            games_pref[game] += 1
        else:
            games_pref[game] = 1

print(games_pref)

# trovare il massimo
maxi= 0
maxi_game = ""
for game,game_count in games_pref.items():
    if game_count > maxi:
        maxi = game_count
        maxi_game = game
print(maxi_game, maxi)
