# Group: The Abstraction Layer
# Course: CS361
# Assignment: 9 - Big Pool Implementation
# Microservice: ASCII Confirmation Generator
# Due Date: 2026-08-10

from random import sample
from time import sleep


REQUEST_FILE = 'ascii_confirmation_generator.txt'


def greet() -> None:
    """
    Greet user and advise request-response format.
    """
    print('\nASCII Confirmation Generator Microservice is running.')
    print('Waiting for ASCII request in ascii-confirmation-generator.txt.')
    print('Request is 1-line string of desired confirmation notification.')
    print('Response is multi-line string of ASCII art containing input.\n')


def get_file_text() -> str:
    """
    Return text from REQUEST FILE if exists, else create empty file and
    return empty string.
    """
    try:
        with open(REQUEST_FILE, 'r') as f:
            file_text = f.read().strip()
    except FileNotFoundError:
        with open(REQUEST_FILE, 'w') as f:
            f.write('')
        file_text = ''
    
    return file_text


def validate_request(file_text: str, last_file_text: str) -> bool:
    """
    Return true if text from REQUEST FILE exists, does not match the last
    file text, and has only one newline; else, return false.
    """
    newline_count = len(file_text.split('\n'))
    if file_text != '' and file_text != last_file_text and newline_count == 1:
        return True
    else:
        return False


def generate_ascii(file_text: str) -> str:
    """
    Return string of ASCII art that confirms success of the operation
    described by the input string.
    """
    ascii = [
        '                  ____                              _',
        '                 / ___| _   _  ___ ___ ___  ___ ___| |',
        '                 \\___ \\| | | |/ __/ __/ _ \\/ __/ __| |',
        '                  ___) | |_| | (_| (_|  __/\\__ \\__ \\_|',
        '                 |____/ \\__,_|\\___\\___\\___||___/___(_)\n',
        '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n',
        'The following operation completed successfully:\n',
        file_text + '\n',
        '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n'
    ]
    return '\n'.join(ascii)


def process_request(file_text: str, last_file_text: str) -> str:
    """
    Return response based on request or return original file text if the
    request is invalid.
    """
    if validate_request(file_text, last_file_text) is True:
        print('Request received: ' + file_text)
        response = generate_ascii(file_text)
        with open(REQUEST_FILE, 'w') as f:
            f.write(response)
        print('Response sent: \n' + response)
        return response
    else:
        return file_text


def run_microservice() -> None:
    """
    Start microservice as a continuous process.
    """
    greet()

    last_file_text = ''
    while True:
        file_text = get_file_text()
        last_file_text = process_request(file_text, last_file_text)
        sleep(1)


if __name__ == '__main__':
    run_microservice()
