sentence = input("Sentence: ")
letters = 0
for i in sentence:
    if i.isalpha():
        letters += 1

print(letters)