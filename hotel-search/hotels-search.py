from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    What are the best hotel offers during my trip to Paris?
    '''
    # Get all offers in Paris
    response = amadeus.shopping.hotel_offers.get(cityCode='PAR')
    hotelid = response.data[0]['hotel']['hotelId']

    # Select one hotel and query it for offers
    resp = amadeus.shopping.hotel(hotelid).hotel_offers.get()
    print(resp.data)

except ResponseError as error:
    print(error)
