"""
Zarządza plikami szablonów
"""
from core.filemanager import FileManager


class TemplateManager:
    """
    Plik menedżera szablonów
    """
    @staticmethod
    def get_template(category, template="basic", output_json=False):
        """
        Odczytuje konkretny plik tekstowy z argumentami
        TODO: przejść do ulepszonego FileManagera
        """
        path = f"templates/{category}/{template}.txt"
        if output_json:
            return FileManager.load_json_file(path)
        return FileManager.read_file(path).strip().split()
