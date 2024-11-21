# command b / j /shifff x
def copyright(func):
    def new_func():
        print("@as;alkfjalk")
        func()

    return new_func()


@copyright
def smile():
    print("😄")


@copyright
def angry():
    print("😡")


@copyright
def love():
    print("🥰")
