class Test(object):
    _w = 'w'
    __wf = 'hehe'
    w = 'normal'
    def __init__(self):
        self.mf = 'mf'
        # self.__wf = 'haha'

tes = Test()
print(Test.w)
print(tes._w)
# print(tes.__wf) #
print(tes._Test__wf)
