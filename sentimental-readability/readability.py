sentence = input("Sentence: ")
letters = 0
words = 1
sentences = 0
for i in sentence:
    if i.isalpha():
        letters += 1
    if i.isspace():
        words += 1
    if i in ['!','.','?']:
        sentences += 1
index = 0.0588 * (words/letters) - 0.296 * S - 15.8
print(index)