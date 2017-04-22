#!/usr/bin/env python

import time
import sys
import random
import os

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write('\n')

def evaluate(response):
	switcher = {
		"help": "try one of the following commands:\nhelp, start, end, exit, go",
		"start": "starting now",
		"end": "ending now",
		"exit": "exiting",
		"go": "go"
	}
	delay_print(switcher.get(response, "nothing"))

def poems():
	p1 = ("Roses are red\n"
		  "Violets are red\n"
		  "Tulips are red\n"
		  "The grass is red\n"
		  "Oh, shit\n"
		  "The garden is on fire"
		  )

	p2 = ("test test one two three\n"
		  "testing one two three test test\n"
          "hey is this thing on"
		 )

	p3 = ("It wasn't until after\n"
		"I poured the second cup\n"
		"that I realized\n"
		"I was alone."
		)

	p4 = ("Pee pee pee pee\n"
		"Pee pee pee pee\n"
		"I would like to urinate\n"
		"I would like to urinate\n"
		"I would like to urinate\n"
		"I would like to urinate\n"
		"I would like to urinate\n"
		"I would like to urinate\n"
		)

	p = [p1, p2, p3, p4]
	return random.choice(p)


def get_input():
	response = raw_input("> ")
	if response == 'poem':
		print ""
		delay_print("Here is a poem:")
		print ""
		delay_print(poems())
		time.sleep(1)
		print ""
		print ""
		delay_print("...")
		delay_print("I hope you enjoyed my poem. You can hear more by typing 'poem' again. Or to continue with the presents please respond to the previous question...")
		response = raw_input("> ")
	return response



def main():

	# Introduction

	print(chr(27) + "[2J")
	
	delay_print("Hello. I am [error] AIDAN.")
	print ""
	delay_print("This is an acronym for Artificially Intelligent Distributor of All Nice things.")
	print ""
	delay_print("I also recite poetry. Type 'poem' at any time if you would like to hear a poem.")
	print ""
	delay_print("Anyway.")
	print ""
	delay_print("I have been programmed to reveal where your presents are.")
	delay_print("But you need to first verify who you are. Please answer the following simple question...")
	delay_print("")

	# Verification

	delay_print("What is your name?")
	response = get_input()
	while response != 'smelly wife':
		delay_print("No...")
		delay_print("Hint: The nickname that celebrates your highly impressive olfactory senses")
		response = get_input()

	delay_print("Excellent. Nobody but you could have known that.")
	delay_print("I am satisfied that you are Josephine Grobstein Walker...")
	print ""
	delay_print("Happy [error] birthday!")
	time.sleep(1)
	print ""



	# dress and shirt

	delay_print("Your first present can't get enough protein...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("You should find a question attached to this present. Please provide your answer here to get your next clue:")
	response = get_input()
	while response != 'wiltshire':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""



	# unfinished jumper

	delay_print("Your second present is lying in a pool of vomit...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("Sorry it's not finished yet! Did you find the question underneath it? Please provide your answer here to get your next clue:")
	response = get_input()
	while response != 'no':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""



	# underwear

	delay_print("Your third present is feeling extremely cold...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("Well done you found it!")
	delay_print("Maybe you would like to warm them up?")
	delay_print("heh heh heh heh heh heh heh heh heh heh heh heh heh heh")
	delay_print("heh heh heh heh heh heh heh heh heh heh heh heh heh heh")
	delay_print("heh heh heh heh heh heh heh heh heh heh heh heh heh heh")
	delay_print("heh heh heh heh heh heh heh heh heh heh heh heh heh heh")
	delay_print("heh heh heh heh heh heh heh heh heh heh heh heh heh heh")
	delay_print("heh heh heh heh heh heh heh heh heh heh heh heh heh heh")
	delay_print("heh heh heh heh heh heh heh heh heh heh heh heh heh heh")
	print ""
	time.sleep(1)
	delay_print("[ERROR]")
	time.sleep(1)
	delay_print("Sorry I don't know what came over me.")
	delay_print("You should find a question attached to this present. Please provide your answer here to get your next clue:")
	response = get_input()
	while response != 'south america':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""



	# t shirt

	delay_print("Your fourth present is in a puzzling situation...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("Great! You should find a question attached to this present. Please provide your answer here to get your next clue:")
	response = get_input()
	while response != '9':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""



	# earrings

	delay_print("Your fifth present is in a drawer in your bedroom")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("Great! You should find a question attached to this present. Please provide your answer here to get your next clue:")
	response = get_input()
	while response != 'potato herder':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""



	# Phone case

	delay_print("Your sixth present is in the employment sleeve")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("Great! You should find a question attached to this present. Please provide your answer here to get your next clue:")
	response = get_input()
	while response != 'O':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""



	# bicycle

	delay_print("The route to your seventh and final present will surely annoy Huxley...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()



	# end

	delay_print("That's all the presents for this year! I hope [error] you had a nice time.")
	print ""
	time.sleep(1)
	delay_print("Happy birthday!")
	delay_print("AIDAN LOVES YOU")
	delay_print("ERROR.")
	delay_print("ERROR.")
	delay_print("SEG FAULT.")
	exit()

if __name__ == "__main__":
	main()

