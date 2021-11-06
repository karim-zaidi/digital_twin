from Element import Element

class Window(Element):

    def __init__(self, p1, p2):
        super().__init__(p1,p2)

    
    # Change the representation into something more readable
    def __repr__(self):
        return f"{self.__class__.__name__}({self.p1}, {self.p2})"