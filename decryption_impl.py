import re
from Crypto.Cipher import AES
import base64


def parse_logs_for_static(logs):
    lines = logs.splitlines()
    results = []
    for line in lines:
        if "||" in line:
            result = re.search('\|\|(.*)\|\|', line)
            results.append(result.group(1))
    return results


def decrypt_static_logs(text, key, code_book):
    key = base64.decodebytes(bytes(key,'utf-8'))
    for line in text:
        decoded_line = base64.decodebytes(bytes(line, 'utf-8'))
        #padded_line = pad(decoded_line)
        aes = AES.new(key, AES.MODE_CBC, 's needs to be 16')

        decrypted = aes.decrypt(decoded_line)
        print(decrypted)



block_size = AES.block_size
def pad(plain_text):
    """
    func to pad cleartext to be multiples of 8-byte blocks.
    If you want to encrypt a text message that is not multiples of 8-byte blocks,
    the text message must be padded with additional bytes to make the text message to be multiples of 8-byte blocks.
    """
    number_of_bytes_to_pad = block_size - len(plain_text) % block_size
    ascii_string = chr(number_of_bytes_to_pad)
    padding_str = number_of_bytes_to_pad * ascii_string
    padded_plain_text =  plain_text + padding_str
    return padded_plain_text