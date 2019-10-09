from huffman import HuffmanCoding


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
        return self.__cert_contents


def main():
    decrypter = Decrypter("lib/key.pem")
    out = decrypter.decrypt("test")
    # print(out)

    huffman_coding = HuffmanCoding("lib/sample.txt")

    output_path = huffman_coding.compress()
    huffman_coding.decompress(output_path)


if __name__ == "__main__":
    main()
