from typing import Callable
from typing.io import TextIO

import pandas as pd

from exceptions import CSVFIleError, PCDConversionError
from settings.pcd_config import PCD_HEADER


def convert_to_pcd(filename: str, input_dir: str, output_dir: str, file_fun: Callable) -> str:
    """
    Convert csv file to pcd file
    Args:
        filename: CSV file name
        input_dir: Directory where input file is present
        output_dir: Directory where converted file to be stored
        file_fun: function to get the reference of output file

    Returns:
        Success message with csv filename

    Raises:
        CSVFIleError: CSV file error
        PCDConversionError: Error while converting csv to pcd
    """
    # Check if filename endswith csv or not
    if not filename.endswith(".csv"):
        raise CSVFIleError("File not ends with .csv extension")

    # Strip .csv from filename
    filename_without_ext = filename.rstrip(".csv")

    try:
        # Read the CSV file as dataframe which is separated by space
        df = pd.read_csv(f"{input_dir}/{filename}", sep=" ", header=None)

    except Exception as e:
        raise CSVFIleError(e)

    # initially file reference will be None
    file_ref = None

    try:
        # Get the file reference
        file_ref = file_fun(filename_without_ext, output_dir)  # type: TextIO

        # Get the header string and modify it considering the no. of lines in CSV
        pcd_header = PCD_HEADER.format(width=len(df), points=len(df))

        # write pcd_header to the new file
        file_ref.write(pcd_header)

        # Add each row of dataframe to new pcd file
        for row in df.iterrows():
            data = row[1]
            file_ref.write(f"{data[0]} {data[1]} {data[2]} {data[3]}\n")

        # Close the file
        file_ref.close()

    except Exception as e:
        # In case of any exception, if file reference exists, close it
        if file_ref:
            file_ref.close()

        # Raise the error
        raise PCDConversionError(e)

    return f"Successfully converted the file {filename}"
