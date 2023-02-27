import os
import pytest
# from typing import Generator


@pytest.fixture
def character() -> dict:
    return {
        "id": 19,
        "name": "Antenna Rick",
        "status": "unknown",
        'species': 'Human',
        'type': 'Human with antennae',
        'gender': 'Male',
        'origin': {'name': 'unknown', 'url': ''},
        'location': {'name': 'unknown', 'url': ''},
        'image': 'https://rickandmortyapi.com/api/character/avatar/19.jpeg',
        'episode': ['https://rickandmortyapi.com/api/episode/10'],
        'url': 'https://rickandmortyapi.com/api/character/19',
        'created': '2017-11-04T22:28:13.756Z'
    }


@pytest.fixture
def character_path() -> str:
    # path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
    # "characters")
    return ("/home/py-athos/python/Trilhas/PythonAvancado/Aula16_Pytest/py" +
            "tests/pytests/characters")


@pytest.fixture
def character_file_path() -> str:
    return ("/home/py-athos/python/Trilhas/PythonAvancado/Aula16_Pytest/py" +
            "tests/pytests/characters/Antenna Rick.txt")


@pytest.fixture
def create_folder(character_path) -> None:
    if not os.path.exists(character_path):
        os.mkdir(character_path)


@pytest.fixture
def create_file(character_file_path, character) -> str:
    if not os.path.exists(character_file_path):
        with open(character_file_path, "w") as f:
            f.write(str(character))
        return (f"\n{character['name']} created! \n\n"
                + f"Path: {character_file_path}\n")
    else:
        return f"{character_file_path} already exists!"


# @pytest.fixture
# def character_file_write() -> str:
#     file_name = "Antenna Rick.txt"
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     previous_dir = os.path.dirname(dir_path)
#     characters_path = os.path.join(previous_dir, "pytests", "characters")
#     if not os.path.exists(characters_path):
#         os.mkdir(characters_path)

#     character_file = os.path.join(
#         previous_dir, "pytests", "characters", file_name)
#     if not os.path.exists(character_file):
#         with open(character_file, "w") as f:
#             f.write(str(character))

#     return character_file


@pytest.fixture
def character_file_read() -> str:
    file_name = "Antenna Rick.txt"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    previous_dir = os.path.dirname(dir_path)
    characters_path = os.path.join(previous_dir, "pytests", "characters")
    if not os.path.exists(characters_path):
        os.mkdir(characters_path)

    character_file = os.path.join(
        previous_dir, "pytests", "characters", file_name)
    if not os.path.exists(character_file):
        with open(character_file, "w") as f:
            f.write(str(character))
    print(os.path.exists(character_file))
    return file_name


@pytest.fixture
def character_file_delete() -> None:
    file_path = ("/home/py-athos/python/Trilhas/PythonAvancado/Aula16_Pyt"
                 + "est/pytests/pytests/characters/Antenna Rick.txt")
    if os.path.exists(file_path):
        os.remove(file_path)

# tentar Generator depois

# @pytest.fixture
# def character_file_read() -> Generator[str, None, None]:
#     file_name = "Antenna Rick.txt"
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     previous_dir = os.path.dirname(dir_path)
#     characters_path = os.path.join(previous_dir, "pytests", "characters")
#     if not os.path.exists(characters_path):
#         os.mkdir(characters_path)

#     character_file = os.path.join(
#         previous_dir, "pytests", "characters", file_name)
#     if not os.path.exists(character_file):
#         with open(character_file, "w") as f:
#             f.write(str(character))

#     yield file_name

#     # if os.path.exists(character_file):
#     #     os.remove(character_file)
#     print("pamonha")
