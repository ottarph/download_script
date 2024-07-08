

def test_download_gdrive():
    from download import download_gdrive
    from pathlib import Path
    import shutil

    ID_biharm_p2_npy = "1P5MGkW_zkAxu5ikUj5pQ-Bg2AMzsAvS4"
    ID_biharm_p2_tar_gz = "1u7-eJdaMWhuV47dVgKV0bzwD_D4P2ceW"

    download_gdrive(ID_biharm_p2_npy, "downloaded_biharm_p2.npy")
    assert Path("downloaded_biharm_p2.npy").exists()
    Path("downloaded_biharm_p2.npy").unlink()
    
    download_gdrive(ID_biharm_p2_tar_gz, "downloaded_biharm_p2_extracted.tar.gz", extract=True)
    assert Path("downloaded_biharm_p2_extracted").exists() and Path("downloaded_biharm_p2_extracted").is_dir()
    assert Path("downloaded_biharm_p2_extracted.tar.gz").exists()

    Path("downloaded_biharm_p2_extracted.tar.gz").unlink()
    shutil.rmtree("downloaded_biharm_p2_extracted")
    
    download_gdrive(ID_biharm_p2_tar_gz, "downloaded_biharm_p2_extracted.tar.gz", extract=True, rm_archive=True)
    assert not Path("downloaded_biharm_p2_extracted.tar.gz").exists()

    shutil.rmtree("downloaded_biharm_p2_extracted")

    return


def test_download():

    from download import download
    from pathlib import Path
    import shutil

    url = "https://sandbox.zenodo.org/records/77047/files/mm-fsi-w-don-DATA.tar.gz?download=1"

    download(url, "mm-fsi-w-don-DATA.tar.gz", extract=True, rm_archive=True)
    assert Path("mm-fsi-w-don-DATA").exists() and Path("mm-fsi-w-don-DATA").is_dir()
    assert not Path("mm-fsi-w-don-DATA.tar.gz").exists()

    shutil.rmtree("mm-fsi-w-don-DATA")

    return


if __name__ == "__main__":
    test_download_gdrive()
    test_download()
