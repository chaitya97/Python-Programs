import string
import random

class PasswordGenerator:
    def passwordDictionary(self):
        self.length = int(input("Enter password length you want to generate: "))
        print("")
        self.include_letters = str(input("Include letters? (y/n): ")).upper() == 'Y'
        self.include_digits = str(input("Include digits? (y/n): ")).upper() == 'Y'
        self.include_symbols = str(input("Include symbols? (y/n): ")).upper() == 'Y'
    
    def passwordBuild(self):
        self.chars = ''
        if self.include_letters:
            self.chars += string.ascii_letters
        if self.include_digits:
            self.chars += string.digits
        if self.include_symbols:
            self.chars += string.punctuation
    
    def passwordGenerate(self):
        if self.chars:
            password = ''.join(random.choice(self.chars) for _ in range(self.length))
            print("Generated Password:", password)
        else:
            print("You must select at least one character type!")

# Example usage
if __name__ == "__main__":
    pg = PasswordGenerator()
    pg.passwordDictionary()
    pg.passwordBuild()
    pg.passwordGenerate()
