from passlib.hash import pbkdf2_sha256


class Hashing:
    def __init__(self, value):
        self.value = value

    def get_hash(self):
        return pbkdf2_sha256.hash(self.value)

    def verify_hash(self, hashed_value):
        return pbkdf2_sha256.verify(self.value, hashed_value)