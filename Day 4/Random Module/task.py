import random
import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module.my_favouritenumb * random_integer)

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
#
# # random float
# random_float = random.uniform(1, 10)

# head or tail
head_or_tail = random.randint(0, 1)
print(head_or_tail)
if head_or_tail ==0 :
    print('"Head"')
else:
    print('"Tail"')