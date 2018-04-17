import os
from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    What relevant airports are there around a specific location?
    '''
    response = amadeus.reference_data.locations.airports.get(
        longitude=49.000, latitude=2.55)

    for r in response.data:
        print(r['subType'], r['name'], r['detailedName'], r['address'])
except ResponseError as error:
    print(error)
