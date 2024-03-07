def fizzBuzz():
    fizz = stringGenerator("Fizz", 3) # Generates "Fizz" the value provided is a multiple of 3
    buzz = stringGenerator("Buzz", 5) # Generates "Buzz" if the value provided is a multiple of 5
    
    # Maps either a string or value to every number in the range of 1-100, inclusive.
    # If the number is divisible by 3 or 5, returns "Fizz", "Buzz", or 
    # "FizzBuzz" if the value is a multiple of 3 and 5.
    # If the number is not divisible by 3 or 5, the number itself is returned.
    values = map(lambda x: (fizz(x) + buzz(x)) or x, range(1,101))

    # Print all values in the map
    for x in list(values):
        print(x)

# Returns a str if the value provided is a multiple of n
def stringGenerator(str, n):
    # Returns str if the modulo division results in 0, else returns an empty string.
    return lambda y: "" if (y % n) else str

if __name__ == "__main__":  
    fizzBuzz()