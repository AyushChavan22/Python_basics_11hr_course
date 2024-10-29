def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in farenheit:- "))
c = f_to_c(f)
print(f"The temperature in degree celcius is:- {round(c,2)}°C")