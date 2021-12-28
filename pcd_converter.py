from typing import Callable
from typing.io import TextIO

import pandas as pd

from exceptions import CSVFIleError, PCDConversionError
from settings.pcd_config import PCD_HEADER
from utilities import get_new_file_reference


def convert_to_pcd(filename: str, input_dir: str, output_dir: str, file_fun: Callable) -> str:
    if not filename.endswith(".csv"):
        raise CSVFIleError("File not ends with .csv extension")

    filename_without_ext = filename.rstrip(".csv")

    try:
        df = pd.read_csv(f"{input_dir}/{filename}", sep=" ")

    except Exception as e:
        raise CSVFIleError(e)

    file_ref = None

    try:
        file_ref = file_fun(filename_without_ext, output_dir)  # type: TextIO
        pcd_header = PCD_HEADER.format(width=len(df), points=len(df))

        file_ref.write(pcd_header)

        for row in df.iterrows():
            data = row[1]
            file_ref.write(f"{data[0]} {data[1]} {data[2]} {data[3]}\n")

        file_ref.close()

    except Exception as e:
        raise PCDConversionError(e)

    if file_ref:
        file_ref.close()

    return f"Successfully converted the file {filename}"


# if __name__ == '__main__':
#     convert_to_pcd("RecFile_1_1_20210709_130249_RealSense2_Device_1_RGBCamera_Color_15.csv", "testdir", "testdir/newdir", get_new_file_reference)
