from decryption import Decrypter
import unittest


class DecryptionTest(unittest.TestCase):

    def test_main(self):
        decrypter = Decrypter("lib/key.pem")
        cert = decrypter.decrypt("test")
        self.assertTrue(cert)


if __name__ == "__main__":
    unittest.main()
