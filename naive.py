class NaiveStringMatch(object):

    def __init__(self, text, word):
        self.text = text
        self.word = word
        self.text_len = len(text)
        self.word_len = len(word)

    def search(self): 
        indices = list()
        for i in range(self.text_len - self.word_len + 1): 
            j = 0
            for j in range(self.word_len): 
                if (self.text[i + j] != self.word[j]): 
                    break
            if (j == self.word_len - 1):  
                print("Pattern found at index ", i); indices.append(i)
        return indices
    
matcher = NaiveStringMatch("How is it going", "going")
print(matcher.search())