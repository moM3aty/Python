#you can do your decoration by @<name>

def announce(f):
    def wrraper():
        print("About to run function...")
        f()
        print("Done with the function")
    return wrraper

@announce
def hello():
    print("Hello world!")

hello()
