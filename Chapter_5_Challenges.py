# 1: Create List of musicians

musicians = ["ELO", "Earth Wind and Fire", "Muse"]

# print(musicians)


# 2: Create List of Tuples of long/lat for places you've been

locations = []

pittsburgh = (-79.995888, 40.440624)
punta_cana = (-68.405472, 18.582010)
sicily = (14.015356, 37.599995)

locations.append(pittsburgh)
locations.append(punta_cana)
locations.append(sicily)

# print(locations)


# 3: Create Dict with self attributes

personal = {"height": 67,
            "weight": 205,
            "eye": "hazel",
            "hair": "brown"}

# print(personal)
# print(personal["eye"])


# 4: Allow user to ask for personal info from #3

# question = input("What info would you like from me? ")

# if question in personal:
#     print(personal[question])
# else:
#     print("Sorry, I don't have that info.")


# 5: Create dict mapping musicians to list of their songs

music = {"ELO": ["Mr. Blue Sky", "Turn To Stone", "Don't Bring Me Down"],
         "Queen": ["Don't Stop Me Now", "Bohemian Rhapsody"]}

print(music)
