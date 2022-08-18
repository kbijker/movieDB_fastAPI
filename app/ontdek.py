from tmdbv3api import TMDb, Discover
from token_request import tokenv3

tmdb = TMDb()

tmdb.api_key = tokenv3

discover = Discover()

# What are the most popular TV shows?

show = discover.discover_tv_shows({"sort_by": "popularity.desc"})

for p in show:
    print(p.name)
    print(p.overview)
    print("")