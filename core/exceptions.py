class VillageInitException(Exception):
    """
    Błąd podczas inicjalizacji wsi
    """


class VillageNotExists(Exception):
    """
    Wieś została dodana do bota, ale nie jest skonfigurowana w pliku konfiguracyjnym
    """


class InvalidGameStateException(Exception):
    """
    Błąd podczas odczytu stanu gry wsi
    """


class InvalidUnitTemplateException(Exception):
    """
    Wybrany szablon jednostek dla wsi jest brakujący lub uszkodzony
    """


class InvalidJSONException(Exception):
    """
    Plik JSON, który próbuję odczytać, jest uszkodzony i nie można go przeanalizować
    """


class FileNotFoundException(Exception):
    """
    Plik, który próbuję odczytać, nie istnieje, a powinien być tam
    """


class UnsupportedPythonVersion(Exception):
    """
    Próbujesz uruchomić bota ze staromodną wersją Pythona
    Aktualizacja do Python3 rozwiąże ten problem
    """
