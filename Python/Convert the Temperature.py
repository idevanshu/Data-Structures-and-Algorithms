def convertTemperature(celsius):
    """
    Formula:-
    Celsius to Kelvin: k = c + 273.15
    Celsius to Fahrenheit:
    """
    kelvin = float(celsius + 273.15)
    fahrenheit = float(celsius * 9/5 + 32)
    return [kelvin,fahrenheit]