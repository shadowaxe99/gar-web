
import os
from cryptography.fernet import Fernet

class SecureStorage:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        cipher_text = self.cipher_suite.encrypt(data.encode())
        return cipher_text

    def decrypt_data(self, cipher_text):
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()

    def save_data(self, filename, data):
        encrypted_data = self.encrypt_data(data)
        with open(filename, 'wb') as file:
            file.write(encrypted_data)

    def load_data(self, filename):
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        return self.decrypt_data(encrypted_data)
