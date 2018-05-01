import string
from abc import ABC, abstractmethod

import os

import pyaes
from io import BytesIO, StringIO


class Cipher(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def generate_key(self):
        pass

    @abstractmethod
    def encrypt(self, key, message):
        pass

    @abstractmethod
    def decrypt(self, key, ciphertext):
        pass

    @abstractmethod
    def get_key_size(self):
        pass

class AesCBC128(Cipher):
    def __init__(self) -> None:
        super().__init__()

    def generate_key(self):
        return os.urandom(16)

    def generate_iv(self):
        return os.urandom(16)

    def encrypt(self, key, message):
        instream = BytesIO(message)
        outstream = BytesIO()

        iv = self.generate_iv()
        aes = pyaes.AESModeOfOperationCBC(key, iv=iv)

        pyaes.encrypt_stream(aes, instream, outstream)

        ciphertext = outstream.getvalue()

        instream.close()
        outstream.close()

        return iv+ciphertext


    def decrypt(self, key, ciphertext):

        iv = ciphertext[:16]
        encoded_message = ciphertext[16:]

        instream = BytesIO(encoded_message)
        outstream = BytesIO()
        aes = pyaes.AESModeOfOperationCBC(key, iv)
        pyaes.decrypt_stream(aes, instream, outstream)

        plaintext = outstream.getvalue()

        instream.close()
        outstream.close()

        return plaintext

    def get_key_size(self):
        return 16

