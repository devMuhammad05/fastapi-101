from fastapi import FastAPI

app = FastAPI()

BANDS = [
    {'id': 1, 'name' : 'The kinks', 'genre' : 'Rock'},
    {'id': 2, 'name' : 'Aphex Twin', 'genre' : 'Electronic'},
    {'id': 3, 'name' : 'Slowdive', 'genre' : 'Shoegaze'},
    {'id': 4, 'name' : 'Wu-Tang Clan', 'genre' : 'Hip-Hop'},
]

@app.get('/bands')
async def index() -> list[dict]:
    return BANDS


@app.get('/about')
async def about() -> str:
    return "Great company"