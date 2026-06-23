import json
import os

from core.exceptions import InvalidJSONException, FileNotFoundException


class FileManager:
    """Zapewnia metody do zarządzania plikami i katalogami."""

    @staticmethod
    def get_root():
        """Zwraca katalog główny projektu."""
        return os.path.join(os.path.dirname(__file__), "..")

    @staticmethod
    def get_path(path):
        """Zwraca pełną ścieżkę pliku lub katalogu w projekcie."""
        return os.path.join(FileManager.get_root(), path)

    @staticmethod
    def path_exists(path):
        """Zwraca True, jeśli ścieżka istnieje, False w przeciwnym razie."""
        return os.path.exists(path)

    @staticmethod
    def create_directory(directory):
        """Tworzy katalog, jeśli nie istnieje."""
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def create_directories(directories):
        """Tworzy listę katalogów w katalogu głównym, jeśli nie istnieją."""
        root_directory = FileManager.get_root()
        for directory in directories:
            directory = os.path.join(root_directory, directory)
            FileManager.create_directory(directory)

    @staticmethod
    def list_directory(directory, ends_with=None):
        """Zwraca listę plików w katalogu. Jeśli ends_with jest określony, tylko pliki kończące się wskazanym ciągiem zostaną zwrócone."""
        full_path = os.path.join(FileManager.get_root(), directory)
        files = os.listdir(full_path)
        if ends_with:
            files = [f for f in files if f.endswith(ends_with)]
        return files

    @staticmethod
    def __open_file(path, mode="r"):
        """Otwiera plik w określonym trybie. Prywatne - NIE UŻYWAĆ poza filemanager."""
        full_path = os.path.join(FileManager.get_root(), path)
        try:
            # Use explicit UTF-8 for text modes to avoid encoding issues
            if 'b' in mode:
                return open(full_path, mode)
            return open(full_path, mode, encoding='utf-8')
        except:
            raise FileNotFoundException

    @staticmethod
    def read_file(path):
        """Odczytuje zawartość pliku i zwraca dane. Zwraca None, jeśli plik nie istnieje."""
        full_path = os.path.join(FileManager.get_root(), path)

        if not FileManager.path_exists(full_path):
            return None

        with FileManager.__open_file(full_path) as file:
            return file.read()

    @staticmethod
    def read_lines(path):
        """Odczytuje zawartość pliku i zwraca linie. Zwraca None, jeśli plik nie istnieje."""
        full_path = os.path.join(FileManager.get_root(), path)

        if not FileManager.path_exists(full_path):
            return None

        with FileManager.__open_file(full_path) as file:
            return file.readlines()

    @staticmethod
    def remove_file(path):
        """Usuwa plik, jeśli istnieje."""
        full_path = os.path.join(FileManager.get_root(), path)

        if FileManager.path_exists(full_path):
            os.remove(full_path)

    @staticmethod
    def load_json_file(path, **kwargs):
        """Ładuje plik JSON i zwraca dane. Zwraca None, jeśli plik nie istnieje."""
        full_path = os.path.join(FileManager.get_root(), path)

        if not FileManager.path_exists(full_path):
            return None

        with FileManager.__open_file(full_path) as file:
            try:
                return json.load(file, **kwargs)
            except json.decoder.JSONDecodeError:
                raise InvalidJSONException

    @staticmethod
    def save_json_file(data, path, **kwargs):
        """Saves data to a JSON file. If the file does not exist, it will be created."""
        full_path = os.path.join(FileManager.get_root(), path)

        with FileManager.__open_file(full_path, mode="w") as file:
            json.dump(data, file, indent=2, sort_keys=False, **kwargs)

    @staticmethod
    def copy_file(src_path, dest_path):
        """Copies a file from the source path to the destination path."""
        full_src_path = os.path.join(FileManager.get_root(), src_path)
        full_dest_path = os.path.join(FileManager.get_root(), dest_path)

        if not FileManager.path_exists(full_src_path):
            return False

        with FileManager.__open_file(full_src_path) as src_file:
            with FileManager.__open_file(full_dest_path, mode="w") as dest_file:
                dest_file.write(src_file.read())
