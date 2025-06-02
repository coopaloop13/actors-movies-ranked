import requests
from django.conf import settings


API_KEY = settings.API_KEY


def search_movies(query: str):
    return [
        {"id": 1, "title": "Example Movie 1"},
        {"id": 2, "title": "Example Movie 2"}
    ]

def search_actor(actor_name: str):

    actor_list = requests.get(
        "https://api.themoviedb.org/3/search/person",
            params={
                "query": actor_name,
                "include_adult": "false",
                "language": "en-US",
                "page": 1
            },
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "accept": "application/json"
            }
        )

    return actor_list

def get_actor_movies(actor_id: str):
    actor_movie_list = requests.get(
        f"https://api.themoviedb.org/3/person/{actor_id}/movie_credits?language=en-US",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "accept": "application/json"
            }
        )

    return actor_movie_list