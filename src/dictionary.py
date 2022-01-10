import src.validator as validator

class Dictionary:
    def __init__(self, filename):
        self.filename = filename
        self.f = None
    
    def __iter__(self):
        self.f = open(self.filename, "r")
        return self

    def __next__(self):
        while(True):
            word = self.f.readline().strip()

            if not word:
                raise StopIteration

            if not validator.Validator.invalid_format(word):
                return word
    
    def __del__(self) -> None:
        if self.f:
            self.f.close()