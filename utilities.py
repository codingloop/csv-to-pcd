import time
from os.path import exists as file_exists

from typing.io import TextIO

from settings.configurations import PCD_FILE_EXTENSION


def get_new_file_reference(file_name: str, output_dir: str) -> TextIO:
    complete_file_name = f"{output_dir}/{file_name}.{PCD_FILE_EXTENSION}"
    return open(complete_file_name, "w")


def get_new_file_ref_without_overwrite(file_name: str, output_dir: str) -> TextIO:
    complete_file_name = f"{output_dir}/{file_name}.{PCD_FILE_EXTENSION}"

    if file_exists(complete_file_name):
        current_timestamp = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
        new_file_name = f"{file_name}_{current_timestamp}"
        return get_new_file_reference(new_file_name, output_dir)

    return get_new_file_reference(file_name, output_dir)


if __name__ == '__main__':
    """ Only for testing, run os.mkdirs(testdir) first"""
    f1 = get_new_file_reference("test1", "testdir")
    f1.close()

    f2 = get_new_file_ref_without_overwrite("test1", "testdir")
    f2.close()

