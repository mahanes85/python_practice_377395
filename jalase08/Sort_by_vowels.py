names = []

def count_vowels(name):
    count = 0
    vowels = "aeouiAEOUI"
    for letters in name:
        if letters in vowels:
            count += 1
    return count

while True:
    name = input("enter name :")
    if name == "quit":
        break
    names.append(name)

names = sorted(names, key=count_vowels, reverse=True)

print(names)