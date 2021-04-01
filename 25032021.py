family=["Berasap", "Moreen", "Wendella", "Wallace", "Waynezeera","Alyssa"]
family.append("Avygail")
family.append("Ivy")
family.remove("Ivy")

for member in family:
    print(member)

import random
r2 = random.choice(family)
print(r2, "is my lucky person")

