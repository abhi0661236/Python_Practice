# This program converts kelvin temprature to fahrenheit.

def kelvinToFahrenheit(temprature):
    assert (temprature >= 0),"Colder than 0 kelvin"
    return ((temprature-273)*28)+32

result = kelvinToFahrenheit(273)
print(result)

result = kelvinToFahrenheit(505.78)
print(result)

result = kelvinToFahrenheit(-5)
print(result)