# Take input in celcius and print its equivalent in fahrenheit and kelvin.
temp_celcius =int(input("Enter temperature in celcius: "))

temp_farenheit =(temp_celcius * 9/5) + 32
temp_kelvin =(temp_celcius + 273.15)

print("Temperature in Farenheit: ",temp_farenheit)
print("Temperature in Kelvin: ",temp_kelvin)