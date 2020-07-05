
class IterableActions:

    def __init__(self):
        print("Starting Iterables")


    def createGenerators(self):

        for x in [1,2,3,4]:
            print(f"Item: {x }")

        my_list = [1, 2, 3, 4]
        # Get an iterator
        iterable = iter(my_list)

        # Loop until StopIteration is raise
        while True:
            try:
                # Ask for next item in iterable
                x = next(iterable)
                print(x)
            except StopIteration:
                break

iteras = IterableActions()
iteras.createGenerators()