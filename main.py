import os
import sys
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Union

from pcd_converter import convert_to_pcd
from settings.configurations import INPUT_DIR, OUTPUT_DIR, PARALLEL_NUMBER_OF_RUNS, OVERWRITE_EXISTING
from utilities import get_files_chunk, iterable_for_threading, list_of_files, get_new_file_reference, \
    get_new_file_ref_without_overwrite


def execute_pcd_conversion(input_dir: str = INPUT_DIR, output_dir: str = OUTPUT_DIR,
                           threads: Union[int, str] = PARALLEL_NUMBER_OF_RUNS) -> None:
    threads = int(threads)

    file_fun = get_new_file_ref_without_overwrite

    if OVERWRITE_EXISTING:
        file_fun = get_new_file_reference

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(convert_to_pcd, list_of_files(input_dir), iter(lambda: input_dir, None),
                               iter(lambda: output_dir, None), iter(lambda: file_fun, None),
                               chunksize=threads)

        for result in results:
            print(result)


def get_argv_as_dict() -> dict:
    key_dict = dict()
    for item in sys.argv[1:]:
        k, v = item.split("=")
        kwargs[k] = v

    return key_dict


if __name__ == '__main__':
    kwargs = get_argv_as_dict()
    execute_pcd_conversion()
