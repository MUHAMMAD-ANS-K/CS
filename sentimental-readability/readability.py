sentence = input("Text: ")
letters = 0
words = 1
sentences = 0
for i in sentence:
    if i.isalpha():
        letters += 1
    if i.isspace():
        words += 1
    if i in ["!", ".", "?"]:
        sentences += 1
L = (letters / words) * 100
S = (sentences / words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
