from validator import lib

host_id = input("Host ID: ")
while not lib.host_id_validator(host_id):
    print("Expression is invalid! Try again")
    host_id = input("Host ID: ")
else:
    host_id = int(host_id)

beds = input("Number of beds: ")
while not lib.beds_validator(beds):
    print("Expression is invalid! Try again")
    beds = input("Beds: ")
else:
    beds = int(beds)

number_reviews = input("Number of reviews: ")
while not lib.number_reviews_validator(number_reviews):
    print("Expression is invalid! Try again")
    number_reviews = input("Numbers of reviews: ")
else:
    host_id = int(number_reviews)

country = input("Country: ")
while not lib.country_validator(country):
    print("Expression is invalid! Try again")
    country = input("Country: ")
