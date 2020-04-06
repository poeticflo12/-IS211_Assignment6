#!python3



def convertCelsiusToKelvin(data):
    """Function to convert celsius to kelvin"""
    return (data + 273.15)

def convertCelsiusToFarenheit(data):
    """Function to convert celsius to farenheit"""
    result=round((data * 9/5) + 32,2)
    return(result)

def convertFarenheitToCelsius(data):
    """Function to farenheit to celsius"""
    return round((data - 32) * 5/9,2)

def convertFarenheitToKelvin(data):
    """Function to farenheit to kelvin"""
    return round((data + 459.67)  * 5/9,2)

def convertKelvinToCelsius(data):
    """Function to kelvin to celsius"""
    return round((data - 273.15),2)

def convertKelvinToFarenheit(data):
    """Function to kelvin to farenheit"""
    return round((data * 9/5) - 459.67,2)