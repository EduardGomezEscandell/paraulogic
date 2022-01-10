import sys
from src.dictionary import Dictionary
from src.validator import Validator

if __name__ == "__main__":
    lletra_central = "u"      if len(sys.argv) < 2 else sys.argv[1]
    altres_lletres = "aelmnt" if len(sys.argv) < 3 else sys.argv[2]
    
    diec      = Dictionary("data/diec.txt")
    validator = Validator(lletra_central, altres_lletres)  

    for entry in diec:
        validator.validate_entry(entry)

    # Resultats
    print(f"S'ha trobat {validator.word_count()} paraul{'a' if validator.word_count()==1 else 'es'}:")
    i = 1
    for word in validator.word_list():
        print(f"{i:>3}. {word}")
        i += 1