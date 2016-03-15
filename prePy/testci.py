class ASmallClass:
    def __init__(self,s):
        self.data=s
    def haha(self):
        print('haha from A Small Class\n')

class ASDC(ASmallClass):
    def __init__(self,s):
        self.data=s
    def haha(self):
        print('haha from a derived class\n')

x=ASmallClass('Hatsune-Miku')
y=ASDC('shit')
y.haha()
x.haha()
y.haha()
