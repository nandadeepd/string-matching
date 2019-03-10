# from utils.util import inputs

import cProfile

class KMP(object):
	def __init__(self, pattern, text):
		self.pat = pattern; self.txt = text
		self.M = len(pattern); self.N = len(text)
		self.matches = list()

	def KMPSearch(self): 
		j = 0 # index counter for pattern 
		lps = self.computeLPSArray() # build the longest prefix table 
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
		return self.matches

	def computeLPSArray(self):
        
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
		return lps


def main():
    # txt = "cagcggggaagggtctttaccgcttaggcctctaattctatcggttcggacggcgccaacttatatctcatacgcagcccaaccgcccactaagccgtcgagccaacctagaatgagcaggacgatccacctgcaatgccactcgagataatctcgaaggcttctagccctgacagtttccgtgagccgaatacagttacccacaattcttcaatcacggtcatctatctgatttggaaggctacatgtcgtccgtctcaggcactggcatgtcgacgttctaattggtctaaccacatgttgctctgctactcgcgcgagccccttaatagatgtaccatggcggcatcaccaaccgtgtcgttagctggaaaggcggctcacatcaatgagcgcgcgagtgataaaccaaacgatctaagccccgcacgataaaaaatagtggttacaggttcaccgtccgatgaccccttgtttgttatcagtgagcaagaaaaactcagcgccaccacaaatagtgtgggtgtatgaggtggaggggatagggctcatacaacaagggctgttacactacggtttaatcggtaatccccgtaagatgcgttatgagggcgccatctctatcacgaaaacctgttctataaccggggtgcacgcccactgattcgtcttcacggtattctcacacataaagccgcatattcgcgattggtgctctctagcgtggtggggcctgttacttcccgcatcctgggggtactaaggtcaactggtagtagctccacatcgaccttccgctgaaacagactgggtattacgcgcccggctgatagcaacgtaagatgccaggttaggacgcagtgtacgatatcggcaaagtagaactaccagtagttaatcctacaaagaccctcgtatcactaagagcctttatatatgcctataattgagtccgttggccaccgtggcatgactaccacatagtggtctctatccatcg"; pat = "gact";
    # kmp = KMP(pat, txt)
    cProfile.run('txt = "cagcggggaagggtctttaccgcttaggcctctaattctatcggttcggacggcgccaacttatatctcatacgcagcccaaccgcccactaagccgtcgagccaacctagaatgagcaggacgatccacctgcaatgccactcgagataatctcgaaggcttctagccctgacagtttccgtgagccgaatacagttacccacaattcttcaatcacggtcatctatctgatttggaaggctacatgtcgtccgtctcaggcactggcatgtcgacgttctaattggtctaaccacatgttgctctgctactcgcgcgagccccttaatagatgtaccatggcggcatcaccaaccgtgtcgttagctggaaaggcggctcacatcaatgagcgcgcgagtgataaaccaaacgatctaagccccgcacgataaaaaatagtggttacaggttcaccgtccgatgaccccttgtttgttatcagtgagcaagaaaaactcagcgccaccacaaatagtgtgggtgtatgaggtggaggggatagggctcatacaacaagggctgttacactacggtttaatcggtaatccccgtaagatgcgttatgagggcgccatctctatcacgaaaacctgttctataaccggggtgcacgcccactgattcgtcttcacggtattctcacacataaagccgcatattcgcgattggtgctctctagcgtggtggggcctgttacttcccgcatcctgggggtactaaggtcaactggtagtagctccacatcgaccttccgctgaaacagactgggtattacgcgcccggctgatagcaacgtaagatgccaggttaggacgcagtgtacgatatcggcaaagtagaactaccagtagttaatcctacaaagaccctcgtatcactaagagcctttatatatgcctataattgagtccgttggccaccgtggcatgactaccacatagtggtctctatccatcg"; pat = "gact";kmp = KMP(pat, txt);kmp.KMPSearch()')
    # content = ""
    # with open('./datasets/dna-1.txt') as f:
    #     content = f.read()


    

    
    

    

if __name__ == "__main__":
    main()