import os
from datetime import datetime


def save_text(text: str, prefix: str):
    """Esta función guarda un texto en un archivo con un prefijo y la fecha actual

    Args:
        text (str): Text to save
        prefix (str): Prefix reflecting the type of file to save.
    """

    # Get current date with specified format
    date_now = datetime.now().strftime("%Y-%m-%d")
    # Build the file name
    file_name = f"{date_now}-{prefix}.txt"

    # Validates if the file already exists, if so, just save the text, and if not, create the file and save the text
    if os.path.isfile(file_name):
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(text + "\n")
    else:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(text + "\n")


def clear_terminal():
    """This function clears the console"""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux y macOS
        os.system('clear')
