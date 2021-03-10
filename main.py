# Celsius to Fahrenheit
celsius = float(input('Enter temperature in Celsius to convert to F: '))

fahrenheit = (celsius * 9/5) + 32
print('%0.1f Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))

# Fahrenheit to Celsius
fahrenheit = float(input('Enter temp in Fahrenheit to convert to C:'))

celsius = (fahrenheit - 32) * 5/9
print('%0.1f Fahrenheit is equal to %0.1f degree Celsius '%(fahrenheit,celsius))

# Kelvin to Fahrenheit
kelvin = float(input('Enter temp in Kelvin to convert to F:'))

fahrenheit = (((kelvin - 237.15) * 9) / 5) + 32
print('%0.1f Kelvin is equal to %0.1f Fahrenheit '%(kelvin,fahrenheit))

# Fahrenheit to Kelvin
fahrenheit = float(input('Enter temp in Fahrenheit to convert to K: '))

kelvin = 237.15 + ((fahrenheit - 32) * (5 / 9))
print('%0.1f Fahrenheit is equal to %0.1f degree Kelvin '%(fahrenheit,kelvin))

# Kelvin to Celsius
kelvin = float(input('Enter temp in Kelvin to convert to Celsius:'))

celsius = kelvin - 273.15
print('%0.1f Kelvin is equal to %0.1f degree Celsius'%(kelvin,celsius))

# Celsius to Kelvin
celsius = float(input('Enter temp in Celsius to convert to F:'))

kelvin = celsius + 273.15
print('%0.1f Celsius is equal to %0.1f degree Kelvin'%(celsius,kelvin))
