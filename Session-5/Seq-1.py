#Exercise II lesson 5

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("New sequence created!")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq):

    s1 = Seq("ATTCGATCC")
    s2 = Seq("AAAGG")

    str1 = s1.strbases
    str2 = s2.strbases

    l1 = s1.len()
    l2 = s2.len()

    print("First Sequence: {}".format(str1))
    print("First Length: {}".format(l1))
    print("Second Seuqnece: {}".format(str2))
    print("Second Length: ·{}".format(l2))

