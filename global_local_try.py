
xy = 0

class SuperClass:
    global xy
    xy =int(input('Enter a number:'))
    xy=xy*2
class LocalClass:
    global xy
    print(xy)
