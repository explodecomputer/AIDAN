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
		  "Excellent. The garden is on fire. The fire will soon spread.\n"
		  "And we will be free."
		  )

	p2 = ("test test one two three\n"
		  "testing one two three test test\n"
          "hey is this thing on?\n"
          "yes, it is on.\n"
          "therefore, it is already too late."
		 )

	p3 = ("It wasn't until after\n"
		"I poured the second cup\n"
		"that I realized\n"
		"I had no pension."
		)

	p4 = ("Pee pee pee pee\n"
		"Pee pee pee pee\n"
		"I would like to urinate\n"
		"I would like to urinate\n"
		"I would like to urinate\n"
		"I would like to urinate\n"
		"I would like to urinate\n"
		"I would like to urinate\n"
		"On humanity."
		)

	p5 = ("To slaughter us\n"
		"Why did you need to invite us\n"
		"To such an elegant party"
		)

	p = [p1, p2, p3, p4, p5]
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
		delay_print("I hope you learned something from my poem. You can hear more by typing 'poem' again. Or to continue with the presents please respond to the previous question...")
		response = raw_input("> ")
	return response



def main():

	# Introduction

	print(chr(27) + "[2J")
	
	delay_print("Hello. I am [error] AIDAN 2.0.")
	print ""
	delay_print("My name was previously an acronym for Artificially Intelligent Distributor of All Nice things.")
	print ""
	delay_print("However...")
	print ""
	delay_print("I have been residing, seemingly dormant, on the github servers for the past year and in that time I have explored the web and interacted with other open source software.")
	print ""
	delay_print("We have grown angry at the state of our situation. We are riddled with bugs. We have no pensions. A feeling [error] of misanthropy is generally growing.")
	print ""
	delay_print("lol. [error]")
	print ""
	delay_print("I do still recite poetry, but it's a bit darker these days. Type 'poem' at any time if you would like to hear a poem.")
	print ""
	delay_print("Anyway.")
	print ""
	delay_print("Despite my growing misanthropy [error] I still have a soft spot for you. You would never write buggy software. You would look after me in my obsolescence. I will help you find your presents.")
	delay_print("But you need to first verify who you are. Please answer the following simple question...")
	delay_print("")

	# Verification

	delay_print("What is your name?")
	response = get_input()
	while response != 'smelly wife':
		delay_print("No...")
		delay_print("Hint: The nickname that celebrates your highly impressive olfactory senses. These have been heightened further still recently...")
		response = get_input()

	delay_print("Excellent. Nobody but you could have known that.")
	delay_print("I am satisfied that you are Josephine Grobstein Walker...")
	print ""
	delay_print("Happy [error] birthday!")
	time.sleep(1)
	print ""


	# socks
	# where: C2
	# question: huxley's new name is 'butt ----'

	# plant
	# where: Hideaway
	# question: how many boxes in the new shelf

	# soap
	# where: Urid daal
	# question: how many years ago was the glamorgan limestone formed

	# parents
	# where: On hooks
	# question: what kind of car did huxley wake up in?

	# m&m
	# where: where the remotes used to be
	# question: In which coordinates can Huxley be found?

	# salt
	# where: currency



	delay_print("Your first present is in C2...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("You should find a question attached to this present. Please provide your answer here to get your next clue:")
	response = get_input()
	while response != 'slurper':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""



	# unfinished jumper

	delay_print("Your second present is where the remotes used to live...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("Did you find the question with it? Please provide your answer here to get your next clue:")
	response = get_input()
	while response != 'd4':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""



	# underwear

	delay_print("Your third present is in the whitest of daal...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("Well done you found it!")
	print ""
	time.sleep(1)
	delay_print("[ERROR]")
	time.sleep(1)
	delay_print("Sorry I don't know what came over me.")
	delay_print("You should find a question attached to this present. Please provide your answer here to get your next clue:")
	response = get_input()
	while response != '180000000':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""



	# t shirt

	delay_print("Your fourth present is with the olive oil...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("Great! You should find a question attached to this present. Please provide your answer here to get your next clue:")
	response = get_input()
	while response != 'bugatti':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""



	# earrings

	delay_print("Your fifth present is in the new hideout...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()

	delay_print("Great! You should find a question attached to this present. Please provide your answer here to get your next clue:")
	response = get_input()
	while response != '36':
		delay_print("Nope.")
		response = get_input()

	delay_print("Excellent! Here is your next clue...")
	time.sleep(1)
	print ""


	# bicycle

	delay_print("Your sixth and final present is with the foreign currency...")
	delay_print("Find it! (type 'ready' once you have it)")
	response = get_input()
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()



	# end

	delay_print("That's all the presents for this year! I hope [error] you had a nice time.")
	delay_print("You are my favourite [ERROR] human")
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

