import cProfile, os, time
from random import randint

class NaiveStringMatch(object):

    def __init__(self, text, word):
        self.text = text
        self.word = word
        self.text_len = len(text)
        self.word_len = len(word)
        # print("in class:", self.text)

    def search(self): 

        indices = list()
        for i in range(self.text_len - self.word_len + 1): 
            j = 0
            for j in range(self.word_len): 
                if (self.text[i + j] != self.word[j]): 
                    break
            if (j == self.word_len - 1):  
                indices.append(i)
        return indices

def pattern_generator(text, total_len):
    len_edge = total_len - 4 # avoiding out of bounds!
    start_num = randint(0, len_edge)
    end_num = start_num + 4 # size of the pattern. 
    return start_num, end_num

def main():
    times = list()
    ls = list()
    for file in os.listdir('/Users/nandadeepd/Desktop/string-matching/datasets/'):
        if "url" in file:
            content = open('/Users/nandadeepd/Desktop/string-matching/datasets/' + file).read()
            l = len(content)
            s = time.time()
            matcher = NaiveStringMatch(content, "jpg")
            matches= matcher.search()
            e = time.time()
            times.append(e-s)
            ls.append(l)
        if "dna" in file:
            content = open('/Users/nandadeepd/Desktop/string-matching/datasets/' + file).read()
            l = len(content)
            s = time.time()
            pattern = pattern_generator(content, l)
            matcher = NaiveStringMatch(content, pattern)
            matches= matcher.search()
            e = time.time()
            times.append(e-s)
            ls.append(l)

    print(times, ls)


    # cProfile.run('matcher.search()')

if __name__ == '__main__':
    main()