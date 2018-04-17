from amadeus import Client, ResponseError, Location

amadeus = Client()

try:
    '''
    Which cities or airports start with ’LON' characters?
    '''
    response = amadeus.reference_data.locations.get(
        keyword='LON', subType=Location.ANY)

    for r in response.data:
        print(r['name'], r['detailedName'])
except ResponseError as error:
    print(error)
