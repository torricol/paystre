from fastapi import APIRouter, Body


movie_route = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)

movies = [
    {"id": 1, "title": "Inception", "year": 2010},
    {"id": 2, "title": "The Matrix", "year": 1999},
    {"id": 3, "title": "Interstellar", "year": 2014},
]

@movie_route.get("/status", tags=["App"])
def status():
    return {"status": "Servicios LMTF corriendo correctamente"}

@movie_route.get("/movies/", tags=["Movies"])
def get_movies():
    return movies

@movie_route.get("/movies/{movie_id}", tags=["Movies"])
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return {"error": "Movie not found"}

@movie_route.get("/movies/search/", tags=["Movies"])
def search_movies(year: int):
    result = [movie for movie in movies if movie["year"] == year]
    return result

@movie_route.post("/movies/", tags=["Movies"])
def add_movie(
    id: int = Body(), 
    title: str = Body(), 
    year: int = Body()
    ):
    movie = {"id": id, "title": title, "year": year}
    movies.append(movie)
    return movie

@movie_route.put("/movies/{movie_id}", tags=["Movies"])
def update_movie(
    movie_id: int, 
    title: str = Body(), 
    year: int = Body()
    ):
    for movie in movies:
        if movie["id"] == movie_id:
            movie["title"] = title
            movie["year"] = year
            return movie
    return {"error": "Movie not found"}

@movie_route.delete("/movies/{movie_id}", tags=["Movies"])
def delete_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return {"message": "Movie deleted"}
    return {"error": "Movie not found"}
