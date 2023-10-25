class Bird:
    def fly(self):
        print("Flying...")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly.")


class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly.")


# NOTE: bad use example of inheritance to "earn" the method fly.
class Plane(Bird):
    def fly(self):
        print("Plane is taking off...")


def flight_plan(obj):
    obj.fly()


flight_plan(Sparrow())
flight_plan(Ostrich())
flight_plan(Plane())