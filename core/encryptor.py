from cryptography.fernet import Fernet
import os

class GhostEncryptor:
    def __init__(self, k_path="ghost.key"):
        self.k_path = k_path
        self.key = self._get_key()
        self.cipher = Fernet(self.key)

    def _get_key(self):
        if os.path.exists(self.k_path):
            with open(self.k_path, "rb") as f: return f.read()
        key = Fernet.generate_key()
        with open(self.k_path, "wb") as f: f.write(key)
        return key

    def encrypt_data(self, data): return self.cipher.encrypt(data.encode()).decode()

    def encrypt_file(self, path):
        with open(path, "rb") as f: enc = self.cipher.encrypt(f.read())
        with open(path + ".ghost", "wb") as f: f.write(enc)
        os.remove(path)
        print(f"[🛡️] Encrypted & Original Deleted: {path}")