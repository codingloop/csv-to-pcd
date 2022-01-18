import os
import sys
from concurrent.futures.thread import ThreadPoolExecutor
from functools import partial
from typing import Union

from pcd_converter import convert_to_pcd
from settings.configurations import INPUT_DIR, OUTPUT_DIR, PARALLEL_NUMBER_OF_RUNS, OVERWRITE_EXISTING
from utilities import list_of_files, get_new_file_reference, \
    get_new_file_ref_without_overwrite


def execute_pcd_conversion(input_dir: str = INPUT_DIR, output_dir: str = OUTPUT_DIR,
                           threads: Union[int, str] = PARALLEL_NUMBER_OF_RUNS) -> None:
    """
    Convert all the CSV files present in input directory to pcd and stores them in output directory
    Args:
        input_dir: source directory path
        output_dir: directory at which pcd files needs to be stored
        threads: Maximum number of conversion/threads at a time

    Returns:
        None
    """
    # Convert to int in case of passed value is string
    threads = int(threads)

    # Initially file reference function pointed to function which don't over-write existing file
    file_fun = get_new_file_ref_without_overwrite

    # If parameter is set change the reference function pointer
    if OVERWRITE_EXISTING:
        file_fun = get_new_file_reference

    # Create a threadpool executor for parallel processing
    with ThreadPoolExecutor(max_workers=threads) as executor:
        # Create a partial function as 3 parameters will be same for all threads
        target_function = partial(convert_to_pcd, input_dir, output_dir, file_fun)

        # Execute conversion for each csv file in input directory
        results = executor.map(target_function, list_of_files(input_dir), chunksize=threads)

        # Print the results
        for result in results:
            print(result)


def get_argv_as_dict() -> dict:
    """
    Convert arguments passed to dictionary by splitting the arguments at '=' symbol
    Returns:
        Dictionary with arguments as key value
    """
    # Initially dict will be empty
    key_dict = dict()

    # Iterate over all the arguments apart from the script name i.e. sys.argv[0]
    for item in sys.argv[1:]:
        # Split each argument at '='
        k, v = item.split("=")
        # Assign it to the dictionary
        kwargs[k] = v

    # return the final dictionary
    return key_dict


if __name__ == '__main__':
    # Get arguments as key value pairs
    kwargs = get_argv_as_dict()

    # Start conversion process
    execute_pcd_conversion()
