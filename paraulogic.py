import re
import unidecode

lletra_central = "u"
altres_lletres = "aelmnt"


regex = f"^[{altres_lletres}{lletra_central}]*{lletra_central}[{altres_lletres}{lletra_central}]*$"
pattern = re.compile(regex)

print("Patró de cerca:", regex)

found_words = []

with open("valid_words.txt", "r") as wordbank:
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

nwords = len(found_words)
print(f"S'ha trobat {nwords} paraul{'a' if nwords==1 else 'es'}:")
i = 1
for word in found_words:
    print(f"{i:>3}. {word}")
    i += 1
