from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    When is the cheapest date to fly to Paris from Nice without stops?
    '''
    response = amadeus.shopping.flight_dates.get(
        origin='NCE', destination='PAR', duration=1)

    for r in response.data:
        print(r['departureDate'], r['returnDate'], r['price'])

except ResponseError as error:
    print(error)
