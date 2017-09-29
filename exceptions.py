try:
    speed = int(input("What is the airspeed velocity of an unladen swallow? "))
except ValueError:
    print("What? I don't kno-oooooooooooooooo!")
else:
    print("I think a swallow could go faster than {}.".format(speed))
