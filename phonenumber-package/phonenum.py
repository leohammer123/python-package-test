from re import I
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone,carrier
num = input("Enter a phone number")
h_number = phonenumbers.parse(num , None)# parse number to format
country = geocoder.description_for_number(h_number,"en")  # country
print('country :'+ country)
timeZone = timezone.time_zones_for_number(h_number) #time zone
print('time zone : '+ timezone)
Carrier = carrier.name_for_number(h_number, 'en') # carrier
print('carrier :'+ carrier )
isvalid = phonenumbers.is_valid_number(h_number)
print('isvalid:'+ isvalid)
possible = phonenumbers.is_possible_number(h_number)
print('possible:' + possible)

