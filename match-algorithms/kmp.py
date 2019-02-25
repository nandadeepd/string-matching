import cProfile, tqdm
# def pi_table(pattern):
#     pi_len = len(pattern); pi = [0] * pi_len
#     pi[0] = -1; k = -1
#     for i in tqdm.tqdm(range(pi_len)):
#         while (k >= 0) and (pattern[k + 1] != pattern[i]):
#             k = pattern[k]
#         k += 1; pi[i] = k
#     return pi

class KMP(object):
	def __init__(self, pattern, text):
		self.pattern = pattern; self.text = text
		self.len_pattern = len(pattern); self.len_text = len(text)
	
	def kmp_search(self):
		if self.pattern == "":
			return 0  # Immediate match - base case 0
		# print(len(text))
		# Compute longest suffix-prefix table
		lsp = [0]  # Base case 1

		for c in self.pattern[1 : ]:
			j = lsp[-1]  # Start by assuming we're extending the previous LSP
			while j > 0 and c != self.pattern[j]:
				j = lsp[j - 1]
			if c == self.pattern[j]:
				j += 1
			lsp.append(j)
		print("pi table: ", lsp)
		j = 0  # Number of chars matched in pattern
		for i in range(self.len_text):
			while j > 0 and self.text[i] != self.pattern[j]:
				j = lsp[j - 1]  # Fall back in the pattern
			if self.text[i] == self.pattern[j]:
				j += 1  # Next char matched, increment position
				if j == self.len_pattern:
					return i - (j - 1)
		return None  # Not found

def main():
	pattern = "going"
	text = "How is it aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdasfadsbgsdtzesdxndbrgdgvdxvffxdfgxdvfgxdcgxdgxfdgxdrfngsrdbgbvedgxetxdrtxdrtxdvvfgxdfgdxnhxdtxbdfgxdfgxfbgdzftbxrtdg going"
	matcher = KMP(pattern, text)
	print("found at : ", matcher.kmp_search())
	# print(kmp_search("going", "How is it aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdasfadsbgsdtzesdxndbrgdgvdxvffxdfgxdvfgxdcgxdgxfdgxdrfngsrdbgbvedgxetxdrtxdrtxdvvfgxdfgdxnhxdtxbdfgxdfgxfbgdzftbxrtdg going"))
	# cProfile.run('kmp_search("going", "How is it aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdasfadsbgsdtzesdxndbrgdgvdxvffxdfgxdvfgxdcgxdgxfdgxdrfngsrdbgbvedgxetxdrtxdrtxdvvfgxdfgdxnhxdtxbdfgxdfgxfbgdzftbxrtdg going")')

if __name__ == "__main__":
	main ()