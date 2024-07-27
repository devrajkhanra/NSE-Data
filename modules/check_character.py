import sys

def is_letter(char):
    """
    Check if the given character is a letter.

    Parameters:
    char (str): A single character to check.

    Returns:
    bool: True if the character is a letter, False otherwise.

    Raises:
    ValueError: If the input is not a single character.
    """
    if len(char) != 1:
        raise ValueError("Input must be a single character.")
    return char.isalpha()

def get_user_input():
    """
    Prompt the user to continue or exit.

    Returns:
    str: 'Y' to continue or 'N' to exit.

    Raises:
    ValueError: If the user input is not 'Y' or 'N'.
    """
    user_input = input("Do you want to continue? (Y/N): ").strip().upper()
    if user_input not in {'Y', 'N'}:
        raise ValueError("Invalid input. Please enter 'Y' or 'N'.")
    return user_input