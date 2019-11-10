from decryption_impl import *
from decryption import *
import unittest
import os.path


class DecryptionImplTest(unittest.TestCase):

    def test_parse_logs_for_static(self):
        logs = Decrypter.read_file("encrypted_logs.txt")
        logs = parse_logs_for_static(logs)

        self.assertTrue(logs)

    def test_parse_logs_for_dynamic(self):
        logs = Decrypter.read_file("encrypted_logs.txt")
        logs = parse_logs_for_static(logs)

        self.assertTrue(logs)

    def test_decrypt_static_logs(self):
        logs = Decrypter.read_file("encrypted_logs.txt")
        keys = Decrypter.read_file("key.txt")
        key = keys.splitlines()[0]
        iv = keys.splitlines()[1]
        code_book = Decrypter.read_file("codebook.txt")
        static_text = parse_logs_for_static(logs)

        decrypt_static_logs(static_text, key, code_book, iv)

        self.assertTrue(os.path.exists("encrypted_logs.txt"))

    def test_decrypt_dynamic_logs(self):
        logs = Decrypter.read_file("encrypted_logs.txt")
        keys = Decrypter.read_file("key.txt")
        key = keys.splitlines()[0]
        iv = keys.splitlines()[1]
        code_book = Decrypter.read_file("codebook.txt")
        dynamic_text = parse_logs_for_dynamic(logs)

        decrypt_dynamic_logs(dynamic_text, key, iv)

        self.assertTrue(os.path.exists("encrypted_logs.txt"))


if __name__ == "__main__":
    unittest.main()
