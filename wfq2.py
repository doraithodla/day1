import string
import sys

words={}
noise={}

# open a file and read the contents

text = open(sys.argv[1]).read()
noisetext = open(sys.argv[2]).read()


for noiseword in noisetext.split():
	noiseword = noiseword.strip(string.punctuation+string.whitespace).lower()
	noise[noiseword]=1

wfd = {}

for word in text.split():
	word = word.strip(string.punctuation+string.whitespace).lower()
	if word in noise:
		pass
	else:
		
		try:
			wfd[word] += 1
		except:
			wfd[word] = 1

for word in wfd:
	print word, wfd[word]
