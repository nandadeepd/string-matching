import cProfile, os, time
from random import randint


class BoyerMoore(object):


	def __init__(self):
		self.NO_OF_CHARS = 256
		self.matches = list()


	def badCharHeuristic(self, string, size): 
		''' 
		The preprocessing function for 
		Boyer Moore's bad character heuristic 
		'''

		# Initialize all occurence as -1 
		badChar = [-1] * self.NO_OF_CHARS 
		print(string)
		# Fill the actual value of last occurence 
		for i in range(size): 
			print(string[i])
			badChar[ord(string[i])] = i; 

		# retun initialized list 
		return badChar 

	def search(self, txt, pat):
		m = len(pat) 
		n = len(txt) 

		# create the bad character list by calling 
		# the preprocessing function badCharHeuristic() 
		# for given pattern 
		badChar = self.badCharHeuristic(pat, m) 

		# s is shift of the pattern with respect to text 
		s = 0
		while(s <= n - m): 
			j = m - 1
			while j >= 0 and pat[j] == txt[s + j]: 
				j -= 1
			# If the pattern is present at current shift, 
			# then index j will become -1 after the above loop 
			if j < 0: 
				self.matches.append(s)
				s += (m - badChar[ord(txt[s + m])] if s + m < n else 1) 
			else: 
				s += max(1, j - badChar[ord(txt[s+j])]) 
		return self.matches


# Driver program to test above funtion 
def pattern_generator(text, total_len):
    len_edge = total_len - 4 # avoiding out of bounds!
    start_num = randint(0, len_edge)
    end_num = start_num + 4 # size of the pattern. 
    return start_num, end_num

def main():
    times = list()
    ls = list()
    for file in os.listdir('/Users/nandadeepd/Desktop/string-matching/datasets/'):
        # if "url" in file:
        #     content = open('/Users/nandadeepd/Desktop/string-matching/datasets/' + file).read()
        #     l = len(content)
        #     s = time.time()
        #     matcher = BoyerMoore()
        #     matches= matcher.search(content, "jpg")
        #     e = time.time()
        #     times.append(e-s)
        #     ls.append(l)
        if "dna" in file:
            content = open('/Users/nandadeepd/Desktop/string-matching/datasets/' + file).read()
            l = len(content)
            s = time.time()
            pattern = pattern_generator(content, l)
            matcher = BoyerMoore()
            matches= matcher.search(content, pattern)
            e = time.time()
            times.append(e-s)
            ls.append(l)

    print(times, ls)

if __name__ == '__main__': 
	main() 

