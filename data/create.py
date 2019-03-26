import glob
import csv
import re
import numpy as np

char_set = set([])

remove_chars = ['-', '.', '(', ')']

def whitening(line):
	for char in remove_chars:
		line = line.replace(char, ' ')
	line = line.strip('\n').strip().lower()
	return re.sub(' +', ' ', line)

def get_chars(line):
	line = line.replace(' ', '').replace('\\', '')
	return set(line)

def encode_chars(line):
	return [char_set[c] for c in line]


def line_generator():
	for filename in glob.glob('../../haiku-scraper/data/*'):
		if '.csv' in filename:
			with open(filename, 'r') as haiku_file:
				spamwreader = csv.reader(haiku_file)
				for line in spamwreader:
					yield line[0]

		if '.txt' in filename:
			for line in open(filename, 'r'):
				yield line


for line in line_generator():
	line = whitening(line)
	char_set = char_set | get_chars(line)

char_set = {c:i+2 for i,c in enumerate(list(char_set))}
char_set[' '] = 0
char_set['\\'] = 1

data_array = []
for line in line_generator():
	line = whitening(line)
	line = encode_chars(line)
	data_array.append(line)

np.save('data.npy', data_array)

print {v:i for i,v in char_set.iteritems()}