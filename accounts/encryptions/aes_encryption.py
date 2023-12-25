from cryptography.fernet import Fernet

from accounts.encryptions.encryption import EncryptionClass

class AesEncryption (EncryptionClass) :

    secret_Key = ""
    
    def __init__(self, key):
        self.secret_Key = key
        self.cipher_suite = Fernet(self.secret_Key)


    def encrypt(message, self):
        return self.cipher_suite.encrypt(message.encode())

    def decrypt(encrypted_message, self):
        return self.cipher_suite.decrypt(encrypted_message).decode()