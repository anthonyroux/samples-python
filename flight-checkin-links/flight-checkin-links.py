import os
from amadeus import Client, ResponseError

amadeus = Client()

try:
    '''
    What is the URL to my online check-in?
    '''
    response = amadeus.reference_data.urls.checkin_links.get(airline='LH')
    print(response.data)

except ResponseError as error:
    print(error)
