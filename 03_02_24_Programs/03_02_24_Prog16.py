'''
Object :

16.	Write a program that will determine weather when the value of temperature and humidity is provided by the user.
TEMPERATURE(C)      HUMIDITY(%)      WEATHER

      >= 30           >=90          Hot and Humid
      >= 30           < 90            Hot
      <30             >= 90         Cool and Humid
      <30             <90             Cool

'''

temperature = int(input("Enter temperature : "))
humidity = int(input("Enter humidity : "))

if temperature >= 30 and humidity >= 90:
    print("Hot and Humid")
elif temperature >= 30 and humidity < 90:
    print("Hot")
elif temperature < 30 and humidity >= 90:
    print("Cool and Humid")
elif temperature < 30 and humidity < 90:
    print("Cool")
