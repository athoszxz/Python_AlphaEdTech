# Classe que recebe um personagem aleatório da api
# https://rickandmortyapi.com/api/character/ cria um arquivo com o nome do
# personagem e escreve os dados do personagem no arquivo, caso o arquivo já
# exista, ignora a criação e escrita do arquivo, também tem um método que
# recebe um nome de personagem e verifica se o arquivo existe, caso exista,
# retorna o conteúdo do arquivo, caso não exista, retorna uma mensagem de erro.
# Todos os métodos devem ter os trechos inpuros separados em métodos puros.
import random
import requests
import os
from typing import Dict, Callable


class RickAndMorty:
    def __init__(self):
        self.url = "https://rickandmortyapi.com/api/character/"
        self.headers = {"Accept": "application/json"}

    # Método que faz a requisição da api
    def get_data(self) -> Dict[str, str]:
        response = requests.get(self.url, headers=self.headers)
        response.raise_for_status()
        return response.json()["results"]

    # Método privado que cria um caminho para o diretório "characters"
    def __create_character_path(self) -> str:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        character_path = os.path.join(dir_path, "characters")
        return character_path

    # Método privado que cria um caminho para o arquivo
    def __create_character_file_path(self, character_name: str) -> str:
        character_path = self.__create_character_path()
        character_file_path = os.path.join(
            character_path, character_name)
        return character_file_path

    # Método que cria um arquivo e escreve os dados do personagem
    def __write_file(self, character_file: str, character: dict) -> str:
        with open(character_file, "w") as f:
            f.write(str(character))
        return f"\n{character['name']} created! \n\n Path: {character_file}\n"

    # Método que cria o diretório characters
    def create_folder(self, character_path: str) -> None:
        if not os.path.exists(character_path):
            os.mkdir(character_path)

    # Método que cria o arquivo
    def create_file(self, character_file_path: str, character: dict) -> str:
        if not os.path.exists(character_file_path):
            return self.__write_file(character_file_path, character)
        else:
            return f"{character_file_path} already exists!"

    # Método preparado para mockar
    def get_random_character(self, character: dict,
                             character_path: str,
                             character_file_path: str,
                             create_folder: Callable,
                             create_file: Callable) -> str:
        create_folder
        return create_file.__str__()

    def get_api_random_character(self):
        character = random.choice(self.get_data())
        character_name = character["name"]
        file_name = f"{character_name}.txt"
        character_path = self.__create_character_path()
        character_file_path = self.__create_character_file_path(file_name)
        result = self.get_random_character(character,
                                           character_path,
                                           character_file_path,
                                           self.create_folder(character_path),
                                           self.create_file(
                                               character_file_path, character))
        return result

    # Método que lê o arquivo
    def read_file(self, character_file: str) -> str:
        with open(character_file, "r") as f:
            return f.read()

    # Método que verifica se o arquivo existe
    def __get_character_file(self, character_path: str,
                             character_file_path: str) -> str:
        if not os.path.exists(character_path):
            return "Character folder not found"
        elif not os.path.exists(character_file_path):
            return "Character file not found"
        else:
            return self.read_file(character_file_path)

    # Método que pega o conteúdo de um personagem específico se ele existir
    def get_character(self, name: str) -> str:
        file_name = f"{name}.txt"
        character_path = self.__create_character_path()
        character_file_path = self.__create_character_file_path(file_name)
        return self.__get_character_file(character_path, character_file_path)
