# Author: Jeff Ananias
# Course: CS361
# Assignment: 9 - Big Pool Implementation
# Microservice: ASCII Confirmation Generator

import time

REQUEST_FILE = "ascii_confirmation_generator.txt"


def main() -> None:
    """Start microservice as continuous process."""
    greet()
    last_file_text = ""
    while True:
        file_text = get_file_text()
        last_file_text = process_request(file_text, last_file_text)
        time.sleep(0.5)


def greet() -> None:
    """Greet user and advise request-response format."""
    print("\nASCII Confirmation Generator Microservice is running.")
    print("Waiting for ASCII request in ascii-confirmation-generator.txt.")
    print("Request is 1-line string of desired confirmation notification.")
    print("Response is multi-line string of ASCII art containing input.\n")


def get_file_text() -> str:
    """
    Return text from REQUEST FILE if exists; else create empty file and
    return empty string.
    """
    try:
        with open(REQUEST_FILE, "r") as f:
            file_text = f.read().strip()
    except FileNotFoundError:
        with open(REQUEST_FILE, "w") as f:
            f.write("")
        file_text = ""
    return file_text


def is_response_message(file_text: str) -> bool:
    """
    Return True if file_text is response instead of request;
    else return False.
    """
    return bool(len(file_text.split("\n")) > 1)


def generate_ascii(file_text: str) -> str:
    """
    Return string of ASCII art that confirms success of the operation
    described by the input string.
    """
    ascii = [
        "            ____                              _",
        "           / ___| _   _  ___ ___ ___  ___ ___| |",
        "           \\___ \\| | | |/ __/ __/ _ \\/ __/ __| |",
        "            ___) | |_| | (_| (_|  __/\\__ \\__ \\_|",
        "           |____/ \\__,_|\\___\\___\\___||___/___(_)\n",
        "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n",
        "The following operation completed successfully:\n",
        file_text + "\n",
        "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n",
    ]
    return "\n".join(ascii)


def process_request(file_text: str, last_file_text: str) -> str:
    """
    Return response based on request or return original file text if
    request is invalid.
    """
    if file_text != "" and file_text != last_file_text:
        if is_response_message(file_text):
            return file_text
        else:
            print("Request received: " + file_text)
            response = generate_ascii(file_text)
            with open(REQUEST_FILE, "w") as f:
                f.write(response)
            print("Response sent:\n" + response)
            return response
    return last_file_text


if __name__ == "__main__":
    main()
