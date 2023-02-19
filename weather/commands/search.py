from .models import Location

def autocomplete(results: list) -> list:
    return [Location(result) for result in results]