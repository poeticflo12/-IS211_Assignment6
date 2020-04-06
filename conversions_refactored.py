#python3

class ConversionNotPossible(Exception):
    pass


"""store conversion rates in dictionary"""
conversion_rate = dict()
conversion_rate[("Celsius","Kelvin")]= lambda data: '{}'.format(data+273.15)
conversion_rate[("Celsius","Farenheit")]= lambda data: '{}'.format((data * 9/5) + 32)
conversion_rate[("Farenheit","Celsius")]= lambda data: '{}'.format(((data - 32) * 5/9))
conversion_rate[("Farenheit","Kelvin")]= lambda data: '{}'.format((data + 459.67)  * 5/9)
conversion_rate[("Kelvin","Celsius")]= lambda data: '{}'.format((data * 9/5) + 32)
conversion_rate[("Kelvin","Farenheit")]= lambda data: '{}'.format((data * 9/5) - 459.67)
conversion_rate[("Miles","Yards")]= lambda data: '{}'.format(data*1760)
conversion_rate[("Miles","Meters")]= lambda data: '{}'.format(data*1609.344)
conversion_rate[("Yards","Miles")]= lambda data: '{}'.format(data/1760)
conversion_rate[("Yards","Meters")]= lambda data: '{}'.format(data/1.093613)
conversion_rate[("Meters","Yards")]= lambda data: '{}'.format(data*1.093613)
conversion_rate[("Meters","Miles")]= lambda data: '{}'.format(data/1609.344)


def convert(fromUnit, toUnit, value):
    """Function to convert one unit to the other"""
    if (fromUnit==toUnit):
        return value
    elif (fromUnit,toUnit) in conversion_rate:
        rateString = conversion_rate[fromUnit,toUnit]
        rate=rateString(value)
        return float(rate)
    else:
        raise ConversionNotPossible("Incompatible types")

