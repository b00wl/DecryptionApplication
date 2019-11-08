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


def parse_logs_for_dynamic(logs):
    lines = logs.splitlines()
    results = {}
    line_num = 0
    for line in lines:
        if "||" in line:
            text = line[line.rfind('||')+2:]
            if text != "":
                results[text]=line_num
        line_num += 1
    return results


def parse_results_for_padding(text):
    return str(text).split('b\'')[1].split('\\x')[0]


def decrypt_static_logs(text, key, code_book, iv):
    key = base64.decodebytes(bytes(key,'utf-8'))
    iv = base64.decodebytes(bytes(iv, 'utf-8'))
    for encrypted in text:
        decoded_line = base64.decodebytes(bytes(encrypted, 'utf-8'))
        aes = AES.new(key, AES.MODE_CBC, iv)

        decrypted = parse_results_for_padding(aes.decrypt(decoded_line))
        write_static_logs(code_book, decrypted)


def decrypt_dynamic_logs(text, key, iv):
    key = base64.decodebytes(bytes(key,'utf-8'))
    iv = base64.decodebytes(bytes(iv, 'utf-8'))
    for encrypted, line_num in text.items():
        decoded_line = base64.decodebytes(bytes(encrypted, 'utf-8'))
        aes = AES.new(key, AES.MODE_CBC, iv)
        decrypted = aes.decrypt(decoded_line)

        #decrypted = parse_results_for_padding(aes.decrypt(decoded_line))
        write_dynamic_logs(decrypted, line_num)


def write_static_logs(code_book, text):
    lines = code_book.splitlines()
    for line in lines:
        unencrypted = line.split('-')
        if text in unencrypted[1]:
            write_static_logs_to_file(unencrypted[0])


def write_static_logs_to_file(text):
    with open('unecrypted_logs.txt', 'a') as unencrypted_logs:
        unencrypted_logs.write(text + '\n')


def write_dynamic_logs(text, line_num):
    with open('unecrypted_logs.txt', 'r') as unencrypted_logs:
        data = unencrypted_logs.readlines()

    # now change the 2nd line, note that you have to add a newline
    data[line_num] = data[line_num].strip() + str(text) + '\n'

    # and write everything back
    with open('unecrypted_logs.txt', 'w') as unencrypted_logs:
        unencrypted_logs.writelines(data)