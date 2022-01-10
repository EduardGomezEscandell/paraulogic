import re
import unidecode

class Validator:
    def __init__(self, center:str, others:str) -> None:
        print("Lletra central:", center)
        print("Lletres extra: ", others)
        regex = f"^[{others}{center}-]*{center}[{others}{center}]*$"
        self.pattern = re.compile(regex)
        self.words = {}
    
    def validate_word(self, word_simple: str, as_is: str = None) -> bool:
        if(len(word_simple) < 3):
            return

        if not as_is:
            as_is = word_simple

        if self.pattern.match(word_simple):
            
            if word_simple in self.words:
                self.words[word_simple].add(as_is)
            else:
                self.words[word_simple] = set([as_is])
            
            return True
        return False
    
    @classmethod
    def invalid_format(cls: type, word: str):
        return len(word) < 3 or word[0] == "'" or word[0] == "-" or word[-1]=="-"

    def validate_entry(self, entry: str) -> None:
        entry = entry.strip()

        if self.invalid_format(entry):
            return

        entry = re.sub("\[o (\w+)\]", "\\1", entry)
        
        variants = [v.strip() for v in entry.split()]

        for v in variants:            
            value = v
            # if v[0] == "-":
            #     value = variants[0][:-1] + value[1:]

            key = unidecode.unidecode(value).replace("*", "")

            if self.invalid_format(key):
                continue

            self.validate_word(key, value)
    
    def word_count(self) -> int:
        return len(self.words)

    def word_list(self) -> list:
        l = [" o ".join(x) for x in self.words.values()]
        l.sort()
        return l