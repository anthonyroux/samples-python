from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    Where were people flying to from Nice during the last August?
    '''
    response = amadeus.travel.analytics.air_traffic.traveled.get(
        origin='NCE', period='2017-08')
    print(response.data)

except ResponseError as error:
    print(error)
