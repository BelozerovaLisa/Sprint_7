import random
import string

class Helpers:
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_phone_number(self, length):
        random_string = ''.join(str(random.randint(0, 9)) for i in range(length))
        return int(random_string)