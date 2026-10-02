import random

deck = [f"{v}{s}" for s in "\u2660\u2665\u2666\u2663" for v in "6789TJQKA"]
random.seed(2026)
print("Всего карт в колоде:", len(deck))

hand = random.sample(deck, 5)
print("Рука игрока (sample):", hand)

print("Карта дня (choice) :", random.choice(deck))

weights = {"обычная": 70, "редкая": 25, "легендарная": 5}
loot = random.choices(list(weights), weights=list(weights.values()), k=5)
print("Лут (choices, 5 шт.):", loot)

random.shuffle(deck)
print("После shuffle     :", deck[:6], "...")

print("\n--- Раздача 3 игрокам по 5 карт ---")
players = ["Алиса", "Борис", "Вера"]
pool = deck.copy()

# TODO
for p in players:
    cards = random.sample(pool, 5)
    for card in cards:
        pool.remove(card)
    print(f"{p:6s}:", cards)
