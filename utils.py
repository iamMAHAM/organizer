from pathlib import Path
from typing import Union


def get_folder_files_only(folder: Union[str, Path]) -> list[Path]:
    """
    Get all files in a folder
    """
    folder = Path(folder)
    return [f for f in folder.iterdir() if f.is_file()]


def get_folder_folders_only(folder: Union[str, Path]) -> list[Path]:
    """
    Get all folders in a folder
    """
    folder = Path(folder)
    return [f for f in folder.iterdir() if f.is_dir()]


def get_folder_content(folder: Union[str, Path]) -> list[Path]:
    """
    Get all files and folders in a folder
    """
    folder = Path(folder)
    return list(folder.iterdir())


def to_path(path: Union[str, Path]) -> Path:
    """
    Convert a string to a Path object
    """
    return Path(path)
