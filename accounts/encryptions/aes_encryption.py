from cryptography.fernet import Fernet

class AesEncryption ():

    secret_Key = ""
    
    def __init__(self, key):
        self.secret_Key = key
        self.cipher_suite = Fernet(self.secret_Key)

    def aes_encrypt_message(message, self):
        return self.cipher_suite.encrypt(message.encode())

    def aes_decrypt_message(encrypted_message, self):
        return self.cipher_suite.decrypt(encrypted_message).decode()