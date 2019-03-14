# from utils.util import inputs

import cProfile, time, os
from random import randint

class KMP(object):
	def __init__(self, pattern, text):
		self.pat = pattern; self.txt = text
		self.M = len(pattern); self.N = len(text)
		self.matches = list()

	def search(self): 
		search_start_time = time.time()
		j = 0 # index counter for pattern 
		lps, p_time = self.computeLPSArray() # build the longest prefix table 
		print(p_time)
		i = 0 # index counter for text
		while i < self.N: # iterating throught the text
			if self.pat[j] == self.txt[i]: # when there's a character match
				i += 1
				j += 1

			if j == self.M: 
				# print("Found pattern at index " + str(i-j))
				self.matches.append((i - j))
				j = lps[j - 1] 

			elif i < self.N and self.pat[j] != self.txt[i]: # mismatch after j matches
				# Do not match lps[0..lps[j-1]] characters, 
				# they will match anyway 
				if j != 0: 
					j = lps[j-1]
				else: 
					i += 1
		search_end_time = time.time()
		return self.matches, search_end_time - search_start_time, p_time

	def computeLPSArray(self):
		p_start_time = time.time()
		lps = [0] * self.M
		l = 0 # length of the previous longest prefix suffix 
		lps[0] # lps[0] is always 0 
		i = 1

		# the loop calculates lps[i] for i = 1 to M-1 
		while i < self.M: 
			if self.pat[i]== self.pat[l]: 
				l += 1
				lps[i] = l
				i += 1
			else: 
				# This is tricky. Consider the example. 
				# AAACAAAA and i = 7. The idea is similar 
				# to search step. 
				if l != 0: 
					l = lps[l - 1] 
				else: 
					lps[i] = 0
					i += 1
		p_end_time = time.time()
		return lps, p_end_time - p_start_time



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
            matcher = KMP(content, "jpg")
            matches= matcher.search()
            e = time.time()
            times.append(e-s)
            ls.append(l)
        if "dna" in file:
            content = open('/Users/nandadeepd/Desktop/string-matching/datasets/' + file).read()
            l = len(content)
            s = time.time()
            pattern = pattern_generator(content, l)
            matcher = KMP(content, pattern)
            matches= matcher.search()
            e = time.time()
            times.append(e-s)
            ls.append(l)

    print(times, ls)

    
    

    

if __name__ == "__main__":
    main()