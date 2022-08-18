import fastapi
import uvicorn
from Movie_DB import get_movie
from movie_model import MovieModel

app = fastapi.FastAPI()

@app.get('/')
def index():
    return {
        "message": "Website FastAPI index-site",
        "usage": " Call fast API /api/movie/{title}"
    }

@app.get('/api/movie/{title}', response_model=MovieModel)
async def movie_search(title: str):
    movie = await get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=404)
    return movie.dict()

if __name__ == '__main__':
    uvicorn.run(app)


#bron: https://www.youtube.com/watch?v=qQNGw_m8t0Y