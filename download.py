import requests
import shutil

from pathlib import Path
from os import PathLike


def download_core(url: str, filename: Path, params: dict = None):

    with requests.get(url, params=params, stream=True) as r:
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return

def extract_archive(archive: PathLike, rm_archive: bool = False):
    archive = Path(archive)

    if archive.suffix in (".tar", ".zip"):
        shutil.unpack_archive(archive, archive.with_suffix(""))
    elif archive.suffix == ".gz" and archive.with_suffix("").suffix == ".tar":
        shutil.unpack_archive(archive, archive.with_suffix("").with_suffix(""))
    else:
        raise ValueError(f"Cannot extract {archive.suffix} files")
    
    if rm_archive:
        archive.unlink()

    return

def download(url, filename, extract: bool = False, rm_archive: bool = False):
    filename = Path(filename)

    Path(filename).unlink(missing_ok=True)

    download_core(url, filename)
    extract_archive(filename, rm_archive) if extract else None

    return


def download_gdrive(ID: str, filename: PathLike, extract: bool = False, rm_archive: bool = False):
    filename = Path(filename)
    Path(filename).unlink(missing_ok=True)

    url = "https://docs.google.com/uc?export=download"

    download_core(url, filename, params={"id": ID})        
    extract_archive(filename, rm_archive) if extract else None

    return

