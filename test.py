import sys
sys.path.append("../src")

from src.validator import Validator
from src.dictionary import Dictionary
import unidecode

# Dades de 2021-01-09
lletra_central = "u"
altres_lletres = "aelmnt"

diec =      Dictionary("data/diec.txt")
validator = Validator(lletra_central, altres_lletres)  

for entry in diec:
    validator.validate_entry(entry)
obtained = set(validator.words.keys())

with open("data/paraulogic_2021_01_09.txt") as f:
    testdata = set([unidecode.unidecode(x).strip().replace("*", "") for x in f.readlines()])

retval = 0

missing = list(testdata.difference(obtained))
if len(missing):
    missing.sort()
    print("Missing words are:")
    for w in missing:
        print(f" {w.replace('*', '·')}")
    retval -= 1

wrong = list(obtained.difference(testdata))
if len(wrong):
    wrong.sort()
    print("Wrong words are:")
    for w in wrong:
        print(f" {w.replace('*', '·')}")
    retval -= 2

exit(retval)

