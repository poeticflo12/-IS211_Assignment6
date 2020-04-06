import unittest
import conversions


class Tests(unittest.TestCase):
    # test cases for all the tests
    known_values_celsius_to_kelvin = ((0, 273.15), (1, 274.15), (2, 275.15), (3, 276.15), (4, 277.15))
    known_values_celsius_to_farenheit = ((0, 32), (1, 33.8), (2, 35.6), (3, 37.4), (4, 39.2))
    known_values_farenheit_to_celsius = ((32, 0), (33.8, 1), (35.6, 2), (37.4, 3), (39.2, 4))
    known_values_farenheit_to_kelvin = ((32, 273.15), (41, 278.15), (50, 283.15), (59, 288.15), (68, 293.15))
    known_values_kelvin_to_celsius = ((273.15, 0), (274.15, 1), (275.15, 2), (276.15, 3), (277.15, 4))
    known_values_kelvin_to_farenheit = ((273.15, 32), (278.15, 41), (283.15, 50), (288.15, 59), (293.15, 68))

    def test_celsius_to_kelvin(self):
        """Test to return correct value from celsius to kelvin"""
        for integer, numeral in self.known_values_celsius_to_kelvin:
            result = conversions.convertCelsiusToKelvin(integer)
            self.assertEqual(numeral, result)

    def test_celsius_to_farenheit(self):
        """Test to return correct value from celsius to farenheit"""
        for integer, numeral in self.known_values_celsius_to_farenheit:
            result = conversions.convertCelsiusToFarenheit(integer)
            self.assertEqual(numeral, result)

    def test_farenheit_to_celsius(self):
        """Test to return correct value from farenheit to celsius"""
        for integer, numeral in self.known_values_farenheit_to_celsius:
            result = conversions.convertFarenheitToCelsius(integer)
            self.assertEqual(numeral, result)

    def test_farenheit_to_kelvin(self):
        """Test to return correct value from farenheit to kelvin"""
        for integer, numeral in self.known_values_farenheit_to_kelvin:
            result = conversions.convertFarenheitToKelvin(integer)
            self.assertEqual(numeral, result)

    def test_kelvin_to_celsius(self):
        """Test to return correct value from kelvin to celsius"""
        for integer, numeral in self.known_values_kelvin_to_celsius:
            result = conversions.convertKelvinToCelsius(integer)
            self.assertEqual(numeral, result)

    def test_kelvin_to_farenheit(self):
        """Test to return correct value from kelvin to farenheit"""
        for integer, numeral in self.known_values_kelvin_to_farenheit:
            result = conversions.convertKelvinToFarenheit(integer)
            self.assertEqual(numeral, result)


if __name__ == "__main__":
    unittest.main()