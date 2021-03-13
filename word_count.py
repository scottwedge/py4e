#!/usr/bin/env python3

# Freecodecamp.org challenge
# find the most common word in a sentence


# Functions
def get_sentence():
    s = input("Enter the sentence to be evaluated: ")
    return s

def analyze_sentence(s):
    for j in s.split():
        if j in word_count.keys():
            word_count[j] += 1	# increment existing word count
        else:
            word_count[j] = 1 	# initialize first count of word to 1
    return word_count

def dict_to_list(wc):
    wc_list = [] 
    for k,v in wc.items():
        wc_list.append((v,k))  	# list in (v,k) order to allow sorting later
    return wc_list


# Main code
s = "the clown ran after the car and the car ran into the tent and the tent\
 fell down on the clown and the car"
print("We will evaluate the following sentence: ")
print(s)

word_count = {} # initialize dictionary

word_count = analyze_sentence(s)

word_list = dict_to_list(word_count)

for k,v in word_count.items():
    word_list.append((v,k))  	# swap dictionary k,v order to list v,k order to allow sorting

word_list.sort()   	# sort list numerically by v
most_common_entry = word_list[-1] 	# largest count is last entry in list

(v,k) = most_common_entry
print("Most common word is {}. It occurred {} times.".format(k, v))

