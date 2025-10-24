from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithID

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
async def bands(genre: GenreURLChoices | None = None, has_albums: bool = False) -> list[BandWithID]:
    # return BANDS
    band_list = [ BandWithID(**b) for b in BANDS ]

    if genre:
        band_list = [ b for b in band_list if b.genre.value.lower() == genre.value ]
    
    if has_albums:
        band_list = [ b for b in band_list if len(b.albums) > 0]

    return band_list


@app.get('/bands/{band_id}')
async def band(band_id: int) -> BandWithID:
    band = next((BandWithID(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        return HTTPException(status_code=404, detail='Band not found')
    return band 


@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    band = [b for b in BANDS if b['genre'].lower() == genre.value]
    return band 



@app.post('/bands')
async def create_band(band_data: BandCreate) -> BandWithID:
     
    # get last element from the list
    last_element = BANDS[-1] 

    # last_element_id
    last_element_id = last_element['id']

    # new_id
    new_id = last_element_id + 1

    band = BandWithID(id=new_id, **band_data.model_dump())

    BANDS.append(band.model_dump())

    return band
    