import phonenumbers
from phonenumbers import geocoder
phone_number = phonenumbers.parse("+917092713491")
print(geocoder.description_for_number(phone_number,'en'))