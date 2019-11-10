import argparse
import os
import decryption_impl


class Decrypter:

    def __init__(self, logs, key_file, code_book):
        self.key_file = key_file
        self.code_book = code_book
        self.logs = logs

    @staticmethod
    def read_file(logs) -> str:
        with open(logs) as file_contents:
            __contents = file_contents.read()
        return __contents

    def decrypt(self):
        logs = self.read_file(self.logs)
        keys = self.read_file(self.key_file)
        key = keys.splitlines()[0]
        initialization_vector = keys.splitlines()[1]

        # Static Decryption
        key = self.read_file(self.key_file)
        code_book = self.read_file(self.code_book)
        static_text = decryption_impl.parse_logs_for_static(logs)
        decryption_impl.decrypt_static_logs(static_text, key, code_book, initialization_vector)

        # Dynamic Decryption
        dynamic_text = decryption_impl.parse_logs_for_dynamic(logs)
        decryption_impl.decrypt_dynamic_logs(dynamic_text, key, initialization_vector)



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


def remove_unencrypted_log_file():
    try:
        os.remove('unecrypted_logs.txt')
        with open('unecrypted_logs.txt'):
            pass
    except OSError:
        pass


def main():
    args = parse_args()
    remove_unencrypted_log_file()
    decrypter = Decrypter(args.logs, args.key, args.codebook)
    decrypter.decrypt()


if __name__ == "__main__":
    main()
