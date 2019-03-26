#Exercise Sequence lesson P6

class Seq:

    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def count(self, base):
        n_base = self.strbases.count(base)
        return n_base

    def perc(self, base):
        tl = len(self.strbases)
        if tl > 0:
            nbase = self.count(base)
            perc = round(100.0 * nbase / tl, 1)
        else:
            perc = 0
        return perc

    def call_function(self, name, base=""):
        fn = getattr(self, name)
        value = fn(base)
        return value