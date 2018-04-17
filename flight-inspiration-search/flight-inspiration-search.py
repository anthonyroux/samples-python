from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Where can I fly to from Madrid in the next months for 200€?
    '''
    response = amadeus.shopping.flight_destinations.get(
        origin='MAD', maxPrice=200)
    for r in response.data:
        print(r['destination'], r['departureDate'], r['returnDate'],
              r['price'])
except ResponseError as error:
    print(error)
