class NextWord:
    def __init__(self,datasets):
        self.data = datasets
        self.words = self.data.split()
        self.set_words = set(self.words)
        self.words2id = {k:v for v,k in enumerate(self.set_words)}
        self.id2words = {v:k for k,v in self.words2id.items()}
    def NGram(self,words):
        Gram = []
        for i in range(0,len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            w1 = self.words2id[w1]
            w2 = self.words2id[w2]
            Gram.append((w1,w2))
        return Gram
    def Prop(self,gram):
        pro = {}
        for i in range(len(gram)):
            g1 = gram[i][0]
            g2 = gram[i][1]
            try:
                pro[g1].append(g2)
            except:
                pro[g1] = [g2]
        return pro
    def Prop2(self,prop):
        pro = {}
        for k,v in prop.items():
            values = {}
            for i in range(len(v)):
                try:
                    values[v[i]] = values[v[i]] + (1 /len(self.set_words))
                except:
                    values[v[i]] = (1/len(self.set_words))
            pro[k] = values
        return pro
    def Max(dct):
        sort = sorted(dct.items(),key=  lambda x : x[1],reverse=True)[:5]
        return [i[0] for i in sort]
    def train(self):
        self.gram = NextWord.NGram(self,self.words)
        self.pro1 = NextWord.Prop(self,self.gram)
        self.pro2 = NextWord.Prop2(self,self.pro1)   
    def predict(self,word):
        word = word.split()[0].lower()
        Id = self.words2id[word]
        Id_out = NextWord.Max(self.pro2[Id])
        next_word = [self.id2words[i] for i in Id_out ]
        return next_word