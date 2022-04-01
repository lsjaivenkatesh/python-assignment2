class Counter:
    def __init__(s, v):
        s.v = v

    def increase_one(s):
        s.v = s.v + 1
        return s.v
    def decrease_one(s):
        s.v = s.v - 1
        return s.v
    def get_value(s):
        print(s.v)


x = Counter(1)


# x.get_value()
# x.increase_one()
# x.increase_one()
# x.get_value()
# x.decrease_one()
# x.decrease_one()
# x.get_value()