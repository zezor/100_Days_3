import random

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
random_index = random.randint(0, 4)
#Option 1
print(friends[random_index])

#Option 2
print(random.choice(friends))