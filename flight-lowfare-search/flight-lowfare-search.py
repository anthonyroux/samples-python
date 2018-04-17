import datetime
from amadeus import Client, ResponseError

amadeus = Client()

today = datetime.datetime.now().strftime("%Y-%m-%d")

try:
    '''
    What are the best offers for flights from Madrid to Oporto today?
    '''
    response = amadeus.shopping.flight_offers.get(
        origin='MAD', destination='OPO', departureDate=str(today))

    for resp in response.data:
        for offer in resp['offerItems']:
            print(offer)

except ResponseError as error:
    print(error)
