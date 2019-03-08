class Boyer_Moore(object):
	def __init__(self, pattern, text):
		self.pattern = pattern; self.text = text
		self.len_pattern = len(pattern); self.len_text = len(text)
		