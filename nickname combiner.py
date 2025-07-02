import random
def generate_nicknames(first, last):
    nicknames = [
        first[:3] + last[:3],
        first[0] + last,
        first + last[-2:],
        last[:2] + first[-2:],
        first + str(random.randint(10, 99))
    ]
    return nicknames
print("=== Nickname Combiner ===")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

nicknames = generate_nicknames(first_name, last_name)

print("\nHere are your nickname suggestions:")
for name in nicknames:
    print("-", name)