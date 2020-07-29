from contextlib import contextmanager
import copy

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