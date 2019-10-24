from huffman import HuffmanCoding
import argparse


class Decrypter:
    __decryption_algorithm = ""

    def __init__(self, key_file, code_book, file):
        self.key_file = key_file
        self.code_book = code_book
        self.file = file

    @staticmethod
    def __read_file(file) -> str:
        with open(file) as f:
            __contents = f.read()
        return __contents

    def decrypt(self):
        key = self.__read_file(self.key_file)
        code_book = self.__read_file(self.code_book)
        file = self.__read_file(self.file)

        huffman_coding = HuffmanCoding("lib/sample.txt")
        output_path = huffman_coding.compress()
        huffman_coding.decompress(output_path)


def parse_args():
    """Parse the argument files passed in. Expects fileA, and fileB.
    Returns:
        list: The 2 argument files in args.fileA and args.fileB
    """
    parser = argparse.ArgumentParser(description='Determine if file is malicious')
    parser.add_argument('--key', default='',
                        help="Pass key file name within directory path")
    parser.add_argument('--codebook', default='',
                        help="Pass codebook file name within directory path")

    parser.add_argument('--file', default='',
                        help="Pass file name within directory path")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    decrypter = Decrypter(args.key, args.codebook, args.file)
    decrypter.decrypt()
    # print(out)


if __name__ == "__main__":
    main()


