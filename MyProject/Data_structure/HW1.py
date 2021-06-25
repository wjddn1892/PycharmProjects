wordlist = ['cat', 'dog', 'rabbit']
letterlist = []

for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)

letterlist.sort()

for aletter in letterlist:
    if letterlist.count(aletter) >= 2:
        letterlist.remove(aletter)

print(letterlist)