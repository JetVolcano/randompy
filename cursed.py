import pathlib


def cursed_import(file: pathlib.Path) -> str:
    with file.open() as data:
        return data.read()


exec(cursed_import(pathlib.Path("./example.py")))
print(add(1, 2))