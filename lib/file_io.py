def write_file(file_name, file_content):
    """
    Writes the given content to a file.

    :param file_name: The name of the file (without extension).
    :param file_content: The content to be written to the file.
    """
    with open(f'{file_name}.txt', 'w', encoding='utf-8') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """
    Appends the given content to an existing file.

    :param file_name: The name of the file (without extension).
    :param append_content: The content to be appended to the file.
    """
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as f:
        f.write(append_content)

def read_file(file_name):
    """
    Reads the content of a file.

    :param file_name: The name of the file (without extension).
    :return: The content of the file.
    """
    with open(f'{file_name}.txt', encoding='utf-8') as f:
        return f.read()