
class Indexing:
    """класс индексации файла"""
    def __init__(self, arg):
        self.arg = arg

    def load(self):
        """индексация"""
        memo = {}

        for i in self.arg:
            for j in i:
                if j not in memo.keys():
                    triallist = []
                    c = 0
                    for k in self.arg:
                        if j in k:
                            c = k.count(j)
                            triallist.append((self.arg.index(k), c))
                        else:
                            c = 0
                    memo[j] = triallist
        return memo
