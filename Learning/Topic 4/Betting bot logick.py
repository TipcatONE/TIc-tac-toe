def say_hello(name, city, state):
    if len(name) <= 2:
        return "Hello, " + str(name[0]) + " " + str(name[1]) + "! " + "Welcome to " + city + ", " + state + "!"
    else:
        return "Hello, " + str(name[0]) + " " + str(name[1]) + str(
            name[2]) + "! " + "Welcome to " + city + ", " + state + "!"


say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')

12
9
2
