# Classe que testa os métodos da classe RickAndMorty
import pytest
from pytests.main import RickAndMorty


class TestRickAndMorty:

    @pytest.mark.integration
    def test_get_data(self) -> None:
        assert RickAndMorty().get_data() != []

    # def test_write_file(self, character_file_write, character) -> None:
    #     file_txt = character_file_write
    #     result = RickAndMorty().write_file(file_txt,
    #                                        character)
    #     expected_result = \
    #         f"\n{character['name']} created! \n\n Path: {file_txt}\n"
    #     assert result == expected_result

    @pytest.mark.skip(reason="Test mark.skip")
    def test_fail(self) -> None:
        assert False

    def test_get_random_character(self, character,
                                  character_path, create_folder,
                                  create_file, character_file_read) -> None:
        character_file_read

        character_result = RickAndMorty().get_random_character(character,
                                                               character_path,
                                                               character_path,
                                                               create_folder,
                                                               create_file)
        print(character_result)
        if character_result.endswith("txt\n") or \
                character_result.endswith("already exists!"):
            assert True
        else:
            assert False

    def test_get_character(self, character_file_read) -> None:
        # file_txt = character_file_read.split(".")[0]
        character = RickAndMorty().get_character("Antenna Rick")
        print(character)
        assert character.startswith("{'id':")

    def test_get_character_not_found(self, character_file_read,
                                     character_file_delete) -> None:
        character = RickAndMorty().get_character("fake")
        character_file_delete
        assert character == "Character file not found" or \
            character == "Character folder not found"

    # @pytest.mark.slow
    # def test_read_file(self, character_file_read) -> None:
    #     file_txt = character_file_read
    #     character = RickAndMorty().read_file(file_txt)
    #     assert character.startswith("{'id':")
