a1=input()
a=a1.lower()
vowels=0
consonants=0
digits=0
white=0
b="aeiou"
c="qwrtyplkjhgfdszxcvbnm"
d="1234567890"
e=" "
for i in a:
    if i in b:
        vowels+=1
    if i in c:
        consonants+=1
    if i in d:
        digits+=1
    if i in e:
        white+=1
print("Vowels: {}".format(vowels))
print("Consonants: {}".format(consonants))
print("Digits: {}".format(digits))
print("White spaces: {}".format(white))