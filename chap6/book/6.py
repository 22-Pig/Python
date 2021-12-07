def acronym(phrase):
    return "".join([i[0].upper() for i in phrase.split()])


phrase = input()
print(acronym(phrase))
