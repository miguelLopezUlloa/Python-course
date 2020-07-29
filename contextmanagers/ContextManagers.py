from contextlib import contextmanager
import copy

@contextmanager
def colored_output(color):
    print("Something....before change the color")
    print("\033[%sm" % color, end="")  # lines before the yield associated with __enter__ method
    yield
    print("\033[0m", end="")  # lines after the yield associated with __exit__ method

with colored_output(31):
    print("Now in color!")
    print("So cool.")


my_dict = {"environment": "prod", "db": "MySQL", "nums": [1, 2, 3]}

@contextmanager
def my_patch_dict(my_dict, otrDic):
    cloneDict = copy.copy(my_dict)
    cloneDict["greeting"] = "Hello"
    cloneDict["environment"] = "testing++"
    cloneDict["db"] = "MySQL++"
    cloneDict.update(otrDic)
    print(f"Inside context: {cloneDict}")
    yield
    print(f"After yield: {my_dict}")

with my_patch_dict(my_dict, {"environment": "testing", "name": "Marco"}):
    my_dict["nums"].append(4)
    print(f" After to call the context manager:{my_dict}")








