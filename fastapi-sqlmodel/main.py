from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, Band

app = FastAPI()


BANDS = [
    {'id': 1, 'name': 'The kinks', 'genre': 'Rock'},
    {
        'id': 2,
        'name': 'Aphex Twin',
        'genre': 'Electronic',
        'albums': [{
            'title': 'Selected Ambient Works 85–92',
            'release_date': '1992-11-09'
        }]
    },
    {
        'id': 3,
        'name': 'Slowdive',
        'genre': 'Metal',
        'albums': [{
            'title': 'Souvlaki',
            'release_date': '1993-06-01'
        }]
    },
    {'id': 4, 'name': 'Wu-Tang Clan', 'genre': 'Hip-Hop'},
]


@app.get('/bands')
async def bands() -> list[Band]:
    # return BANDS
    return [
        Band(**b) for b in BANDS
    ]


@app.get('/bands/{band_id}')
async def band(band_id: int) -> Band:
    band = next((Band(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        return HTTPException(status_code=404, detail='Band not found')
    return band 


@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    band = [b for b in BANDS if b['genre'].lower() == genre.value]
    return band 