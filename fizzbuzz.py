def fizzBuzz():
    fizz = stringGenerator("Fizz", 3)
    buzz = stringGenerator("Buzz", 5)

    for x in range(1,101):
        str = x if ((x % 3) and (x % 5)) else fizz(x) + buzz(x)
        print(str)

def stringGenerator(str, n):
    return lambda y: "" if (y % n) else str

fizzBuzz()