from sys import argv

def greet(name):
    """Print 'Hello, [name]'
    name -- a name
    """

    print("Hello, {}!".format(name))

if __name__ == "__main__":
    greet(argv[1])
