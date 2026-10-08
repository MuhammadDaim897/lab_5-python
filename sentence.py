# ask the user to enter a sentence:

sentence=input("Enter a sentence: ")
char=len(sentence)
wrods=len(sentence.split())
vowels=0
space=0
digits=0

for i in sentence:
    if i in "aeiou":
        vowels+=1

    if i==" ":
        space+=1

    if i.isdigit():
        digits+=1

print("characters: ",char)
print("words: ",wrods)
print("How many vowels: ",vowels)
print("spaces: ",space)
print("Digits: ",digits)

