from django.contrib.auth.hashers import BCryptPasswordHasher


class FNPBCryptPasswordHasher(BCryptPasswordHasher):
    def salt(self):
        bcrypt = self._load_library()
        return bcrypt.gensalt(self.rounds, prefix=b"2a")

