# # Position args. (tuple)
# def add(*args):
# #   print(type(args))
#     result = 0
#     for number in args:
#         if type(number) != int:
#             print("Only numbers allowed!")
#             return 0
#         result += number
#     return result


# test = add(3, 5, 6, 2, 1, 4, 5, 1, 7)
# print(test)

# Keyword args. (dict)
def calculate(n, **kwargs):
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


# test = calculate(2, add=3, multiply=5)
# print(test)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R", color="Black", seats="4")
print(
    my_car.make,
    my_car.model,
    my_car.color,
    my_car.seats,
)
