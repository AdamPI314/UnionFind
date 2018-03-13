class UnionFind {
    // Weighted Quick Union With Path Compression
public:
    UnionFind(int n) {
        this->id.assign(n, 0);
        for (int i = 0; i < n; ++i)
            this->id[i] = i;
        this->w.assign(n, -1);
    }
    
public:
    // id
    vector<int> id;
    // weight
    vector<int> w;
    
public:
    int root(int i) {
        // path compression, flat tree, avoid deep tree
        while (i != id[i]) {
            id[i] = id[id[i]];
            i = id[i];
        }
        return i;
    }

    bool find(int p, int q) {
        return root(p) == root(q);
    }
    // weighted quick union, O(N+M lg*N), where lg*N represents number of times needed to 
    // take log of a number unitil reaching 1, almost constant, meaning complexity O(N+M)
    // https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
    void unite(int p, int q) {
        auto i = root(p);
        auto j = root(q);
        
        if (w[i] < w[j]) {
            id[i] = j;
            w[j] += w[i];
        }
        else {
            id[j] = i;
            w[i] += w[j];
        }
    }
    
};
