
import datetime

name = input("Give me your name: ")
age = int (input ("Enter Your Age :"))
now = datetime.datetime.now()
year = now.year

Year_100 = year + (100-age)

print ("Your Age Will be 100 in " + Year_100)


