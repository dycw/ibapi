#!/usr/bin/env python3
from subprocess import check_call
from shutil import copytree
from collections.abc import Iterable
from zipfile import ZipFile
from click import argument, command
from requests import get
from tqdm import tqdm

from tempfile import TemporaryDirectory
from pathlib import Path
from loguru import logger

from sys import stdout

logger.remove()
_ = logger.add(stdout, format="{time:%H:%M:%S} | {message}")


@command()
@argument("url", type=str)
def main(*, url: str) -> None:
    logger.info("Downloading from {url}...", url=url)

    response = get(url, stream=True)
    url_as_path = Path(url)
    zip_file_name = url_as_path.name

    with TemporaryDirectory() as temp:
        temp = Path(temp)
        zip_file = temp.joinpath(zip_file_name)
        with zip_file.open(mode="wb") as fh:
            for data in tqdm(response.iter_content(chunk_size=1024), unit="kB"):
                _ = fh.write(data)

        contents = temp.joinpath("contents")
        with ZipFile(zip_file) as zf:
            zf.extractall(path=contents)

        _check_directory_contents(contents, {"IBJts", "META-INF"})
        _check_directory_contents(
            ibjts := contents.joinpath("IBJts"),
            {"API_VersionNum.txt", "samples", "source"},
        )
        _check_directory_contents(
            source := ibjts.joinpath("source"),
            {"cppclient", "JavaClient", "pythonclient"},
        )
        copytree(source.joinpath("pythonclient"), Path.cwd(), dirs_exist_ok=True)
        _ = check_call(["git", "checkout", "--", ".gitignore"])
        _ = Path("README.md").rename("README.IB-API.md")
        _ = check_call(["git", "checkout", "--", "README.md"])
        _check_directory_contents(
            samples := ibjts.joinpath("samples"),
            {"Cpp", "Java", "Python"},
        )
        _check_directory_contents(
            samples_py := samples.joinpath("Python"),
            {"Testbed"},
        )
        copytree(samples_py.joinpath("Testbed"), "samples", dirs_exist_ok=True)
        with ibjts.joinpath("API_VersionNum.txt").open(mode="r") as fh:
            for line in fh:
                logger.info(line)


def _check_directory_contents(path: Path, names: Iterable[str], /) -> None:
    contents = {p.name for p in path.iterdir()}
    if contents != set(names):
        msg = f"{contents=} != {names=}"
        raise RuntimeError(msg)


if __name__ == "__main__":
    main()
