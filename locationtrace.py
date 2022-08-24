import phonenumbers
from phonenumbers import geocoder , carrier
def loc():
    num1 = input('ENTER THE NUMBER  :')
    num = '+91'+num1
    print('\t ISP NAME\n')
    def contry():
        isp = phonenumbers.parse(num)
        print(geocoder.description_for_number(isp,'en'))
    def ispfinder():
        isp = phonenumbers.parse(num)
        print(carrier.name_for_number(isp,'en'))
    ispfinder()
import json
import geocoder
g = geocoder.ip("192.168.0.103")
