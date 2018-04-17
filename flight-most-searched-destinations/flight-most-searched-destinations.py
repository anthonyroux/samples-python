from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Which were the most searched flight destinations from Nice during last
    August?
    '''
    response = amadeus.travel.analytics.fare_searches.get(
        origin='NCE', sourceCountry='FR', period='2017-08')
    print(response.data)

except ResponseError as error:
    print(error)
