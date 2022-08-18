from tmdbv3api import TMDb, Search
from token_request import tokenv3

def search(query, jaar):

    tmdb = TMDb()
    tmdb.api_key = tokenv3
    search = Search()

    results = search.movies({"query": query, "year": jaar})
    resultaten = {}
    for result in results:
       titel= result.title
       samenvatting= result.overview
       resultaten[query]= (titel, samenvatting)
    return resultaten

#print(search('Matrix', 1999))