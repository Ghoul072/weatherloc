from .models import Location

def autocomplete(results: list[dict]) -> list[Location]:
    """
    Parse search results

    :param results: List of search results returned by the API
    :type results: list[dict]
    :return: list of :class:`~weather.commands.models.location.Location` objects
    :rtype: list[Location]
    """
    return [Location(result) for result in results]