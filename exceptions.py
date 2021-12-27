class CSVFIleError(Exception):
    """
    Raised when file doesn't end with .csv extension or file is not in proper csv format
    """
    pass


class PCDConversionError(Exception):
    """
    Raised whenever csv to pcd conversion process failed
    """
    pass
