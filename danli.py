def singleton(cls):
    isinstance = {}
    def getinstance(*args,**kwargs):
        if cls not in isinstance:
            isinstance[cls] = cls(*args,**kwargs)
        return isinstance[cls]
    return getinstance

@singleton
class MyClass(object):
    pass