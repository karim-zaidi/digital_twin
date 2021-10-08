class Element():

    id = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.id = Element.id
        Element.id += 1
        