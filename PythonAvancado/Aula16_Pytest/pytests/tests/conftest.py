import os
import pytest
from typing import Generator


@pytest.fixture
def character_file_write() -> str:
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

    return character_file


@pytest.fixture
def character_file_read(character_file_write) -> Generator[str, None, None]:
    character_file = character_file_write
    yield character_file

    if os.path.exists(character_file):
        os.remove(character_file)


@pytest.fixture
def character() -> dict:
    return {'id': 19, 'name': 'Antenna Rick',
            'status': 'unknown',
            'species': 'Human',
            'type': 'Human with antennae',
            'gender': 'Male',
            'origin': {'name': 'unknown', 'url': ''},
            'location': {'name': 'unknown', 'url': ''}, 'image':
            'https://rickandmortyapi.com/api/character/ava'
            'tar/19.jpeg', 'episode': ['https://rickandmortyapi.'
                                       'com/api/episode/10'],
            'url': 'https://rick'
            'andmortyapi.com/api/character/19',
            'created': '2017-11-04T22:28:13.756Z'}
