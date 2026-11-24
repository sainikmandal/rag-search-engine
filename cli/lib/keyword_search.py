from .search_utils import load_movies

MAX_RESULTS = 5


def search_movies(query: str, limit: int = MAX_RESULTS) -> list[dict]:
    results = []
    for movie in load_movies():
        if query in movie["title"]:
            results.append(movie)
    results.sort(key=lambda movie: movie["id"])
    return results[:limit]


def search_command(query: str) -> None:
    print(f"Searching for: {query}")
    for i, movie in enumerate(search_movies(query), start=1):
        print(f"{i}. {movie['title']}")
