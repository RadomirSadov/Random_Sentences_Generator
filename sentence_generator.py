import random

names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]


def random_words(words):
    return random.choice(words)


print("Hello this is your first random message.")

while True:
    random_name = random_words(names)
    random_place = random_words(places)
    random_verbs = random_words(verbs)
    random_nouns = random_words(nouns)
    random_adverbs = random_words(adverbs)
    random_details = random_words(details)

    print(f"{random_name} from {random_place} {random_adverbs} {random_verbs} {random_nouns}")
    input("Click [Enter] to generate a new one.")

