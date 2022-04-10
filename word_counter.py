# import operator
import string
import sys

# Open the file in read mode
text = open(sys.argv[1], "r")

# Create an empty dictionary
d = dict()

# Loop through each line of the file
for line in text:
	# Remove the leading spaces and newline character
	line = line.strip()

	# Convert the characters in line to lowercase to avoid case mismatch
	line = line.lower()

	# Remove the punctuation marks from the line
	line = line.translate(line.maketrans("", "", string.punctuation))

	# Split the line into words
	words = line.split(" ")

	# Iterate over each word in line
	for word in words:
		# Check if the word is already in dictionary
		if word in d:
			# Increment count of word by 1
			d[word] = d[word] + 1
		else:
			# Add the word to dictionary with count 1
			d[word] = 1

# Sort items in dictionary in order by value, loop through dictionary
for word, counter in sorted(d.items(), key= lambda v: v[1], reverse=True):

	# Print contents
	print("{} : {}".format(word, counter))

