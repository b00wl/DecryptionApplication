
class Decrypter:

    __cert_contents: str
    __decryption_algorithm = ""

    def __init__(self, cert_file):
        self.cert_file = cert_file
        
    def __read_cert(self):
        with open(self.cert_file) as cert:
            self.__cert_contents = cert.read()

    def decrypt(self, text):
        self.__read_cert()
        print("Decrypting text! " + self.__cert_contents)
        

def main():
    decrypter = Decrypter("lib/key.pem")
    decrypter.decrypt("test")


if __name__ == "__main__":
    main()
