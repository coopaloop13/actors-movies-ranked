from django.http import JsonResponse
from . import moviedb
from . import ranking



def hello_api(request):
    return JsonResponse({"message": "Hello from Actor Movies Ranked backend!"})

def movies_api(request):
    print(request.GET['actor'])
    actor = request.GET['actor']
    movie_list = moviedb.get_actor_movies(actor_name=actor)
 
    return JsonResponse({"response": movie_list.json()})

def actor_api(request):
    firstName = request.GET['firstname']
    lastName = request.GET['lastname']
    actor_list = moviedb.search_actor(actor_name=f"{firstName} {lastName}")
 
    return JsonResponse({"response": actor_list.json()})

def actor_id(request, actor_id):
    print(f"Actor ID: {actor_id}")
    movie_list_response = moviedb.get_actor_movies(actor_id=actor_id)

    movie_list = ranking.rank_movies(movie_list=movie_list_response.json()['cast'])
 
    return JsonResponse({"response": movie_list})
