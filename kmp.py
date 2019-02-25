import cProfile, tqdm
def pi_table(pattern):
    pi_len = len(pattern); pi = [0] * pi_len
    pi[0] = -1; k = -1
    for i in tqdm.tqdm(range(pi_len)):
        while (k >= 0) and (pattern[k + 1] != pattern[i]):
            k = pattern[k]
        k += 1; pi[i] = k
    return pi

def kmp_search(pattern, text):
	if pattern == "":
		return 0  # Immediate match
	print(len(text))
	# Compute longest suffix-prefix table
	lsp = [0]  # Base case
	for c in pattern[1 : ]:
		j = lsp[-1]  # Start by assuming we're extending the previous LSP
		while j > 0 and c != pattern[j]:
			j = lsp[j - 1]
		if c == pattern[j]:
			j += 1
		lsp.append(j)
	print(lsp)
	# Walk through text string
	j = 0  # Number of chars matched in pattern
	for i in range(len(text)):
		while j > 0 and text[i] != pattern[j]:
			j = lsp[j - 1]  # Fall back in the pattern
		if text[i] == pattern[j]:
			j += 1  # Next char matched, increment position
			if j == len(pattern):
				return i - (j - 1)
	return None  # Not found


# print(kmp_search("going", "How is it aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdasfadsbgsdtzesdxndbrgdgvdxvffxdfgxdvfgxdcgxdgxfdgxdrfngsrdbgbvedgxetxdrtxdrtxdvvfgxdfgdxnhxdtxbdfgxdfgxfbgdzftbxrtdg going"))

cProfile.run('kmp_search("going", "How is it aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdasfadsbgsdtzesdxndbrgdgvdxvffxdfgxdvfgxdcgxdgxfdgxdrfngsrdbgbvedgxetxdrtxdrtxdvvfgxdfgdxnhxdtxbdfgxdfgxfbgdzftbxrtdg going")')