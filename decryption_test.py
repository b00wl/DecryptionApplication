from decryption import *
import unittest
import os.path


class DecryptionTest(unittest.TestCase):

    def test_read_file(self):
        logs = Decrypter.read_file("encrypted_logs.txt")
        key_file = Decrypter.read_file("key.txt")
        code_book = Decrypter.read_file("codebook.txt")

        self.assertTrue(logs)
        self.assertTrue(key_file)
        self.assertTrue(code_book)

    def test_remove_unencrypted_log_file(self):
        remove_unencrypted_log_file()
        self.assertFalse(os.path.exists("unencrypted_logs.txt"))


if __name__ == "__main__":
    unittest.main()
