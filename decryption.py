from huffman import HuffmanCoding
import argparse
from decryption_impl import *


class Decrypter:
    __decryption_algorithm = ""

    def __init__(self, logs, key_file, code_book):
        self.key_file = key_file
        self.code_book = code_book
        self.logs = logs

    @staticmethod
    def __read_file(logs) -> str:
        with open(logs) as f:
            __contents = f.read()
        return __contents

    def decrypt(self):
        logs = self.__read_file(self.logs)
        key = self.__read_file(self.key_file)
        test = bytes(key, 'utf-8')
        print(test)
        print(len(test))
        print(type(test))
        code_book = self.__read_file(self.code_book)

        text = parse_logs_for_static(logs)
        decrypt_static_logs(text, key, code_book)


        #huffman_coding = HuffmanCoding("lib/sample.txt")
        #output_path = huffman_coding.compress()
        #huffman_coding.decompress(output_path)


def parse_args():
    """Parse the argument files passed in. Expects fileA, and fileB.
    Returns:
        list: The 2 argument files in args.fileA and args.fileB
    """
    parser = argparse.ArgumentParser(description='Decrypt Log File')
    parser.add_argument('--logs', default='encrypted_logs.txt',
                        help="Pass key file name within directory path")
    parser.add_argument('--key', default='key.txt',
                        help="Pass key file name within directory path")
    parser.add_argument('--codebook', default='codebook.txt',
                        help="Pass codebook file name within directory path")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    decrypter = Decrypter(args.logs, args.key, args.codebook)
    decrypter.decrypt()
    # print(out)


if __name__ == "__main__":
    main()


