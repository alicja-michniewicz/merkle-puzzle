import unittest

from io import BytesIO

from cipher import AesCBC128


class TestAesCipher(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.cipher = AesCBC128()

    def test_pyaes(self):
        import pyaes

        # A 256 bit (32 byte) key
        key = "This_key_for_demo_purposes_only!"

        # For some modes of operation we need a random initialization vector
        # of 16 bytes
        iv = "InitializationVe"



    def test_key_length(self):
        key = self.cipher.generate_key()

        self.assertTrue(self, len(key) in [16,24,32])

    def test_bytes_io(self):
        message = "hello"
        stream = BytesIO(message.encode())
        self.assertEqual(stream.getvalue().decode(), message)
        stream.close()


    def test_encypt_bytes_io(self):
        message = "hello"
        stream = BytesIO(message.encode())
        outstream = BytesIO()
        self.assertEqual(stream.getvalue().decode(), message)


    def test_encrypt_decrypt_unevenBlock(self):
        key = self.cipher.generate_key()

        print(len(key))

        message = "Hello there!! It's a lovely day, don't you think? I love it!"
        ciphertext = self.cipher.encrypt(key, message.encode())

        decrypted_message = self.cipher.decrypt(key, ciphertext)
        print(decrypted_message)

        self.assertEqual(message, decrypted_message.decode())

    def test_encrypt_decrypt_differentKeys(self):
        key = self.cipher.generate_key()
        key2 = self.cipher.generate_key()
        print(len(key))
        print(len(key2))

        message = "Hello there!! It's a lovely day, don't you think? I love it!"
        ciphertext = self.cipher.encrypt(key, message.encode())

        decrypted_message = self.cipher.decrypt(key2, ciphertext)
        print(decrypted_message)

        self.assertEqual(message, decrypted_message.decode())


if __name__ == '__main__':
    unittest.main()
