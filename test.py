import sys

from src.validator import Validator
from src.dictionary import Dictionary
import unidecode

data = [2021, 1, 9] if len(sys.argv) < 4 else [int(x)  for x in sys.argv[1:]]

testdata = {}
lletres = {}
try:
    with open(f"data/paraulogic_{data[0]:>04}_{data[1]:>02}_{data[2]:>02}.txt") as f:

        for i in range(2):
            line = f.readline()
            lletres[line.split(":")[0]] = line.split(":")[-1].replace("\n", "")

        for line in f:
            testdata[unidecode.unidecode(line).strip().replace("*", "").split()[0]] = line
except FileNotFoundError:
    print(f"No s'ha trobat l'arxiu data/paraulogic_{data[0]:>04}_{data[1]:>02}_{data[2]:>02}.txt\n")
    exit(4)

diec =      Dictionary("data/diec.txt")
validator = Validator(lletres["CENTRE"], lletres["EXTRA"])  

for entry in diec:
    validator.validate_entry(entry)
obtained = set(validator.words.keys())

retval = 0

print()

missing = list(set(testdata.keys()).difference(obtained))
if len(missing):
    missing.sort()
    print("Manquen les següents paraules:")
    for w in missing:
        print("-", w)
    retval += 1

wrong = list(obtained.difference(set(testdata.keys())))
if len(wrong):
    wrong.sort()
    print("Sobren les següents paraules:")
    for w in wrong:
        print("-", " o ".join(validator.words[w]))
    retval += 2

if retval == 0:
    print("Cap error!")

exit(retval)

