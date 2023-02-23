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


class RickAndMorty:
    def __init__(self):
        self.url = "https://rickandmortyapi.com/api/character/"
        self.headers = {"Accept": "application/json"}

    # Método impuro que faz a requisição da api
    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        response.raise_for_status()
        return response.json()["results"]

    def __get_character_path(self) -> str:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        character_path = os.path.join(dir_path, "characters")
        return character_path

    def __get_character_file_path(self, character_name: str) -> str:
        character_path = self.__get_character_path()
        character_file_path = os.path.join(
            character_path, character_name)
        return character_file_path

    # Método impuro que cria um arquivo e escreve os dados do personagem
    def write_file(self, character_file: str, character: dict):
        with open(character_file, "w") as f:
            f.write(str(character))
        return f"\n{character['name']} created! \n\n Path: {character_file}\n"

    def __create_folder(self, character_path: str):
        if not os.path.exists(character_path):
            os.mkdir(character_path)

    def __create_file(self, character_file_path: str, character: dict):
        if not os.path.exists(character_file_path):
            return self.write_file(character_file_path, character)
        else:
            return f"{character_file_path} already exists!"

    # Método puro que chama os métodos impuros get_data e write_file
    def get_random_character(self):
        character = random.choice(self.get_data())
        character_name = character["name"]
        file_name = f"{character_name}.txt"
        character_path = self.__get_character_path()
        character_file_path = self.__get_character_file_path(file_name)
        self.__create_folder(character_path)
        return self.__create_file(character_file_path, character)

    # Método impuro que lê o arquivo
    @classmethod
    def read_file(self, character_file: str):
        with open(character_file, "r") as f:
            return f.read()

    def __get_character_file(self, character_path: str,
                             character_file_path: str):
        if os.path.exists(character_path):
            return self.read_file(character_file_path)
        else:
            return f"Character {character_file_path} not found"

    # Método puro que chama o método impuro read_file
    def get_character(self, name: str):
        file_name = f"{name}.txt"
        character_path = self.__get_character_path()
        character_file_path = self.__get_character_file_path(file_name)
        return self.__get_character_file(character_path, character_file_path)
