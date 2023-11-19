import random


class PasswordGenerator:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    c_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '\'~!@#$%^&*()-_=+[]{}\|;:“,<>/?'

    def __init__(self, password_len, numbers_count, symbols_count, capital=False):
        """
            :param password_len: number of letters in password
            :param numbers_count: number of numbers in password
            :param symbols_count: number of symbols in password
            :param capital: is password containing capital letters?
            :return:
        """
        self.capital = capital
        self.symbols_count = symbols_count
        self.numbers_count = numbers_count
        self.password_len = password_len

    def letters_random_generator(self):
        if self.capital:
            self.letters += self.letters.upper()

        letters_len = self.password_len - (self.numbers_count + self.symbols_count)
        return random.choices(self.letters, k=letters_len)

    def numbers_random_generator(self):
        return random.choices(self.numbers, k=self.numbers_count)

    def symbol_random_generator(self):
        return random.choices(self.symbols, k=self.symbols_count)

    def generate(self):
        password = self.letters_random_generator() + self.numbers_random_generator() + self.symbol_random_generator()
        random.shuffle(password)
        return "".join(password)


print(PasswordGenerator(password_len=20, numbers_count=5, symbols_count=2, capital=True).generate())
