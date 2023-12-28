
class Kids:
    pass
    def hi(self):
        print("Hi, I am " + self.name + "!")
    
kid1 = Kids()
kid1.name = "Noah"
Kids.hi(kid1)
kid1.hi()
type(kid1).hi(kid1)

    