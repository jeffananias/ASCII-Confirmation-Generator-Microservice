# Group: The Abstraction Layer
# Course: CS361
# Assignment: 9 - Big Pool Implementation
# Microservice: ASCII Confirmation Generator
# Due Date: 2026-08-10

from random import sample
from time import sleep


REQUEST_FILE = 'ascii-confirmation-generator.txt'


def greet() -> None:
    """
    Greet user and advise request-response format.
    """
    print('\nASCII Confirmation Generator Microservice is running.')
    print('Waiting for ASCII request in ascii-confirmation-generator.txt.')
    print('Request must be a single-line string of text desired for ASCII.')
    print('Response is the input stylized as ASCII.\n')


def get_file_text() -> str:
    """
    TODO: Write docstring
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
    TODO: Write docstring
    """
    newline_count = len(file_text.split('\n'))
    if file_text != '' and file_text != last_file_text and newline_count == 1:
        return True
    else:
        return False


def generate_ascii(file_text: str) -> str:
    """
    TODO: Write docstring
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
    TODO: Write docstring
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
    TODO: Write docstring
    """
    greet()

    last_file_text = ''
    while True:
        file_text = get_file_text()
        last_file_text = process_request(file_text, last_file_text)
        sleep(1)

if __name__ == '__main__':
    run_microservice()
