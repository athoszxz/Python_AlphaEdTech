# Classe que testa os métodos da classe RickAndMorty
import pytest
from pytests.main import RickAndMorty


class TestRickAndMorty:

    def test_get_data(self) -> None:
        assert RickAndMorty().get_data() != []

    def test_write_file(self, character_file_write, character) -> None:
        file_txt = character_file_write
        result = RickAndMorty().write_file(file_txt,
                                           character)
        assert result == \
            f"\n{character['name']} created! \n\n Path: {file_txt}\n"

    @pytest.mark.skip(reason="Testando mark.skip")
    def test_fail(self) -> None:
        assert False

    def test_get_random_character(self) -> None:
        character = RickAndMorty().get_random_character()

        if character.endswith("txt\n") or \
                character.endswith("already exists!"):
            assert True
        else:
            assert False

    def test_get_character(self) -> None:
        character = RickAndMorty().get_character("Antenna Rick")
        assert character.startswith("{'id':")

    @pytest.mark.slow
    def test_read_file(self, character_file_read) -> None:
        file_txt = character_file_read
        character = RickAndMorty().read_file(file_txt)
        assert character.startswith("{'id':")
