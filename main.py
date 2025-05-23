from fastapi import FastAPI

app = FastAPI()

MOVIES = [
    {"ID": 1, "MOVIENAME": "Inception", "GENRE": "Science Fiction", "YEAROFRELEASE": 2010, "BUDGET": 160000000,
     "REVENUE": 836.8, "DIRECTORNAME": "Christopher Nolan", "DURATION": 148, "RATING": "PG-13",
     "PRIMARYLANGUAGE": "English", "POSTER": "Inception.jpg"},
    {"ID": 2, "MOVIENAME": "The Shawshank Redemption", "GENRE": "Drama", "YEAROFRELEASE": 1994, "BUDGET": 25000000,
     "REVENUE": 58.3, "DIRECTORNAME": "Frank Darabont", "DURATION": 142, "RATING": "R", "PRIMARYLANGUAGE": "English",
     "POSTER": "TheShawshankRedemption.jpg"},
    {"ID": 3, "MOVIENAME": "The Dark Knight", "GENRE": "Action", "YEAROFRELEASE": 2008, "BUDGET": 185000000,
     "REVENUE": 1004.6, "DIRECTORNAME": "Christopher Nolan", "DURATION": 152, "RATING": "PG-13",
     "PRIMARYLANGUAGE": "English", "POSTER": "TheDarkKnight.jpg"},
    {"ID": 4, "MOVIENAME": "Forrest Gump", "GENRE": "Drama", "YEAROFRELEASE": 1994, "BUDGET": 55000000,
     "REVENUE": 678.2, "DIRECTORNAME": "Robert Zemeckis", "DURATION": 142, "RATING": "PG-13",
     "PRIMARYLANGUAGE": "English", "POSTER": "ForrestGump.jpg"},
    {"ID": 5, "MOVIENAME": "The Godfather", "GENRE": "Crime", "YEAROFRELEASE": 1972, "BUDGET": 6000000,
     "REVENUE": 245.1, "DIRECTORNAME": "Francis Ford Coppola", "DURATION": 175, "RATING": "R",
     "PRIMARYLANGUAGE": "English", "POSTER": "TheGodfather.jpg"},
    {"ID": 6, "MOVIENAME": "Inglourious Basterds", "GENRE": "War", "YEAROFRELEASE": 2009, "BUDGET": 70000000,
     "REVENUE": 321.5, "DIRECTORNAME": "Quentin Tarantino", "DURATION": 153, "RATING": "R",
     "PRIMARYLANGUAGE": "English", "POSTER": "InglouriousBasterds.jpg"},
    {"ID": 7, "MOVIENAME": "Pulp Fiction", "GENRE": "Crime", "YEAROFRELEASE": 1994, "BUDGET": 8000000, "REVENUE": 214.2,
     "DIRECTORNAME": "Quentin Tarantino", "DURATION": 154, "RATING": "R", "PRIMARYLANGUAGE": "English",
     "POSTER": "PulpFiction.jpg"},
    {"ID": 8, "MOVIENAME": "Titanic", "GENRE": "Romance", "YEAROFRELEASE": 1997, "BUDGET": 200000000, "REVENUE": 2208.4,
     "DIRECTORNAME": "James Cameron", "DURATION": 195, "RATING": "PG-13", "PRIMARYLANGUAGE": "English",
     "POSTER": "Titanic.jpg"},
    {"ID": 9, "MOVIENAME": "Avatar", "GENRE": "Science Fiction", "YEAROFRELEASE": 2009, "BUDGET": 237000000,
     "REVENUE": 2788, "DIRECTORNAME": "James Cameron", "DURATION": 162, "RATING": "PG-13", "PRIMARYLANGUAGE": "English",
     "POSTER": "Avatar.jpg"},
    {"ID": 10, "MOVIENAME": "The Matrix", "GENRE": "Science Fiction", "YEAROFRELEASE": 1999, "BUDGET": 63000000,
     "REVENUE": 465.3, "DIRECTORNAME": "Lana Wachowski, Lilly Wachowski", "DURATION": 136, "RATING": "R",
     "PRIMARYLANGUAGE": "English", "POSTER": "TheMatrix.jpg"},
    {"ID": 11, "MOVIENAME": "The Matrix Reloaded", "GENRE": "Science Fiction", "YEAROFRELEASE": 2003,
     "BUDGET": 150000000, "REVENUE": 742.1, "DIRECTORNAME": "Lana Wachowski, Lilly Wachowski", "DURATION": 138,
     "RATING": "R", "PRIMARYLANGUAGE": "English", "POSTER": "TheMatrixReloaded.jpg"},
    {"ID": 12, "MOVIENAME": "The Matrix Revolutions", "GENRE": "Science Fiction", "YEAROFRELEASE": 2003,
     "BUDGET": 150000000, "REVENUE": 427.3, "DIRECTORNAME": "Lana Wachowski, Lilly Wachowski", "DURATION": 129,
     "RATING": "R", "PRIMARYLANGUAGE": "English", "POSTER": "TheMatrixRevolutions.jpg"},
    {"ID": 13, "MOVIENAME": "The Lord of the Rings: The Fellowship of the Ring", "GENRE": "Fantasy",
     "YEAROFRELEASE": 2001, "BUDGET": 93000000, "REVENUE": 887.5, "DIRECTORNAME": "Peter Jackson", "DURATION": 178,
     "RATING": "PG-13", "PRIMARYLANGUAGE": "English", "POSTER": "TheFellowshipoftheRing.jpg"},
    {"ID": 14, "MOVIENAME": "The Lord of the Rings: The Two Towers", "GENRE": "Fantasy", "YEAROFRELEASE": 2002,
     "BUDGET": 94000000, "REVENUE": 947.7, "DIRECTORNAME": "Peter Jackson", "DURATION": 179, "RATING": "PG-13",
     "PRIMARYLANGUAGE": "English", "POSTER": "TheLordoftheRings.jpg"},
    {"ID": 15, "MOVIENAME": "The Lord of the Rings: The Return of the King", "GENRE": "Fantasy", "YEAROFRELEASE": 2003,
     "BUDGET": 94000000, "REVENUE": 1147.6, "DIRECTORNAME": "Peter Jackson", "DURATION": 201, "RATING": "PG-13",
     "PRIMARYLANGUAGE": "English", "POSTER": "TheReturnoftheKing.jpg"},
    {"ID": 16, "MOVIENAME": "The Silence of the Lambs", "GENRE": "Thriller", "YEAROFRELEASE": 1991, "BUDGET": 19000000,
     "REVENUE": 272.7, "DIRECTORNAME": "Jonathan Demme", "DURATION": 118, "RATING": "R", "PRIMARYLANGUAGE": "English",
     "POSTER": "TheSilenceoftheLambs.jpg"},
    {"ID": 17, "MOVIENAME": "Gladiator", "GENRE": "Action", "YEAROFRELEASE": 2000, "BUDGET": 103000000,
     "REVENUE": 460.5, "DIRECTORNAME": "Ridley Scott", "DURATION": 155, "RATING": "R", "PRIMARYLANGUAGE": "English",
     "POSTER": "Gladiator.jpg"}
]


class Movie():
    ID: int
    MOVIENAME: str
    GENRE: str
    YEAROFRELEASE: int
    BUDGET: int
    REVENUE: float
    DIRECTORNAME: str
    DURATION: int
    RATING: str
    PRIMARYLANGUAGE: str
    POSTER: str

    def __init__(self, ID: int, MOVIENAME: str, GENRE: str, YEAROFRELEASE: int, BUDGET: int,
                 REVENUE: float, DIRECTORNAME: str, DURATION: int, RATING: str,
                 PRIMARYLANGUAGE: str, POSTER: str):
        self.ID = ID
        self.MOVIENAME = MOVIENAME
        self.GENRE = GENRE
        self.YEAROFRELEASE = YEAROFRELEASE
        self.BUDGET = BUDGET
        self.REVENUE = REVENUE
        self.DIRECTORNAME = DIRECTORNAME
        self.DURATION = DURATION
        self.RATING = RATING
        self.PRIMARYLANGUAGE = PRIMARYLANGUAGE
        self.POSTER = POSTER

@app.get("/movies")
async def get_all_movies():
    return MOVIES

@app.get("/movies/{movie_id}")
async def get_movie_by_id(movie_id: int):
    for movie in MOVIES:
        if movie["ID"] == movie_id:
            return movie
    return {"error": "Movie not found"}

@app.get("/moviesgenre")
async def get_movies_by_genre(genre: str):
    filtered_movies = []
    for movie in MOVIES:
        if movie["GENRE"].lower() == genre.lower():
            filtered_movies.append(movie)
    return filtered_movies

@app.post("/movies")
async def create_movie(new_movie: dict):
    MOVIES.append(new_movie)
    return {"message": "Movie created successfully", "movie": new_movie}

@app.put("/movies/{movie_id}")
async def update_movie(movie_id: int, updated_movie: dict):
    for movie in MOVIES:
        if movie["ID"] == movie_id:
            movie.update(updated_movie)
            return {"message": "Movie updated successfully", "movie": movie}
    return {"error": "Movie not found"}