sentence = input("Sentence: ")
letters = 0
words = 0
sentences = 0
for i in sentence:
    if i.isalpha():
        letters += 1
    if i.isspace():
        words += 1
    if i in ['!','.','?']:
        sentences += 1

print(letters,words,sentences)