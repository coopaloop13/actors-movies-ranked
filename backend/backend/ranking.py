


def rank_movies(movie_list):
    ranked_list = []

    ranked_list = sorted(movie_list, key=lambda x: x['popularity'], reverse=True)

    return ranked_list