import httpx
from movie_model import MovieModel
from typing import Optional

async def get_movie(title: str) -> Optional[MovieModel]:

    url = f'https://movieservice.talkpython.fm/api/search/{title}'

    async with httpx.AsyncClient() as client:
        resp: httpx.Response = await client.get(url)
        resp.raise_for_status()
        data = resp.json()

    results = data['hits']
    if not results:
        return None

    movie = MovieModel(**results[0])
    return movie
