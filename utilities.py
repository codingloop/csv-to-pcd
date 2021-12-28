import os
import time
from os.path import exists as file_exists
from typing import Iterable

from typing.io import TextIO

from settings.configurations import PCD_FILE_EXTENSION


def get_new_file_reference(file_name: str, output_dir: str) -> TextIO:
    """
    Create file (overwrite existing if exists) and return reference
    Args:
        file_name: output file name
        output_dir: output file directory

    Returns:
        file reference
    """
    # Create and return file reference
    complete_file_name = f"{output_dir}/{file_name}.{PCD_FILE_EXTENSION}"
    return open(complete_file_name, "w")


def get_new_file_ref_without_overwrite(file_name: str, output_dir: str) -> TextIO:
    """
    If file exists, creates file with timestamp, else simply create file with specified name
    Args:
        file_name: output file name
        output_dir: output file directory

    Returns:
        file reference
    """
    # Evaluate filename
    complete_file_name = f"{output_dir}/{file_name}.{PCD_FILE_EXTENSION}"

    # Check file with the name already exists
    if file_exists(complete_file_name):
        # File already exists, get timestamp and add it to the file
        current_timestamp = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
        new_file_name = f"{file_name}_{current_timestamp}"

        # Create file with new name and return reference
        return get_new_file_reference(new_file_name, output_dir)

    # File not exists, just create and return reference
    return get_new_file_reference(file_name, output_dir)


def list_of_files(path: str) -> Iterable[str]:
    """
    Get list of files in the given path
    Args:
        path: path of the directory or destination directory path

    Returns:
        Iterable object which provides all file names in the given path
    """
    # Iterate over each item in the directory
    for file in os.listdir(path):

        # Check if the item is file or not
        if os.path.isfile(os.path.join(path, file)):
            # Item is a file, so yield it
            yield file
