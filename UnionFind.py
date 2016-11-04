# https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf


class UnionFind(object):
    def __init__(self, n):
        self.id = [None] * n
        for i in range(n):
            self.id[i] = i

    # Abstract method, defined by convention only
    def find(self, p, q):
        raise NotImplementedError("Subclass must implement abstract method")

    # Abstract method, defined by convention only
    def unite(self, p, q):
        raise NotImplementedError("Subclass must implement abstract method")


class QuickFind(UnionFind):
    def __init__(self, n):
        super(QuickFind, self).__init__(n)

    # 1 operation
    def find(self, p, q):
        return self.id[p] == self.id[q]

    # N operations
    def unite(self, p, q):
        pid = self.id[p]
        # change all id with p's id to q's id
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = self.id[q]


class QuickUnion(UnionFind):
    def __init__(self, n):
        super(QuickUnion, self).__init__(n)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def unite(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j


class WeightedQuickUnion(QuickUnion):
    def __init__(self, n):
        super(WeightedQuickUnion, self).__init__(n)
        self.sz = [None] * n
        for i in range(n):
            self.sz[i] = 1

    def unite(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]


class WeightedQuickUnionWithPathCompression(WeightedQuickUnion):
    def __init__(self, n):
        super(WeightedQuickUnionWithPathCompression, self).__init__(n)

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i


if __name__ == '__main__':
    print "haha"

    qf = QuickFind(10)
    qf.unite(1, 3)
    qn = QuickUnion(10)
    qn.unite(1, 3)
    wqn = WeightedQuickUnion(10)
    wqn.unite(1, 3)
    wqnpc = WeightedQuickUnionWithPathCompression(10)
    wqnpc.unite(1, 3)
    print wqnpc.find(1, 3), wqnpc.find(1, 4)
