def fizzBuzz():
    fizz = stringGenerator("Fizz", 3)
    buzz = stringGenerator("Buzz", 5)

    values = map(lambda x: (fizz(x) + buzz(x)) or x, range(1,101))

    for x in list(values):
        print(x)

def stringGenerator(str, n):
    return lambda y: "" if (y % n) else str

fizzBuzz()