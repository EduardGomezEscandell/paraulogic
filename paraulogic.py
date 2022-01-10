import re
import unidecode
import sys

# Valors per defecte
lletra_central = "u"
altres_lletres = "aelmnt"

# Valors d'entrada
if len(sys.argv) == 3:
    lletra_central = sys.argv[1]
    altres_lletres = sys.argv[2]

print("Lletra central:", lletra_central)
print("Lletres extra: ", altres_lletres)

# Cerca
regex = f"^[{altres_lletres}{lletra_central}]*{lletra_central}[{altres_lletres}{lletra_central}]*$"
pattern = re.compile(regex)

found_words = []

with open("diec.txt", "r") as wordbank:
    for word in wordbank:

        if len(word.strip()) < 3:
            continue

        word = word.split()[0].strip()
        if "-" in word or "'" in word:
            continue

        if len(word) < 3:
            continue

        clean_word = unidecode.unidecode(word).lower()

        if pattern.match(clean_word):
            found_words.append(word)

# Resultats
nwords = len(found_words)
print(f"S'ha trobat {nwords} paraul{'a' if nwords==1 else 'es'}:")
i = 1
for word in found_words:
    print(f"{i:>3}. {word}")
    i += 1
