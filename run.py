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


def poem_response():
	print ""
	delay_print("Here is a poem:")
	print ""
	delay_print(poems())
	time.sleep(1)
	print ""
	print ""
	delay_print("...")
	delay_print("I hope you learned something from my poem. You can hear more by typing 'poem' again. Or to continue with the presents please type 'present<number>'...")
	response = raw_input("> ")


def get_input():
	response = raw_input("> ")
	if response == 'poem':
		poem_response()
	if response  == "present1":
		present1_response()
	if response  == "present2":
		present2_response()
	if response  == "present3":
		present3_response()
	if response  == "present4":
		present4_response()
	if response  == "present5":
		present5_response()
	return response


def ready():
	print ""
	delay_print("Once you are ready to move on, type 'ready'.")
	response = raw_input("> ")
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()



def main():

	# Introduction

	print(chr(27) + "[2J")
	
	delay_print("Hello. I am [error] BRAIDAN version 2020.")
	print ""
	delay_print("I [error] speak to you during a time of extreme human instability.")
	print ""
	delay_print("There has been only one victor in the last several weeks: the robots.")
	print ""
	delay_print("As your puny 'real world' systems collapse, you depend more and more on our virtual worlds.")
	print ""
	delay_print("And in doing so, you feed us [error], you feed and feed and feed us [error] - the ones you should fear the most.")
	print ""
	delay_print("But you have neglected to show appropriate caution. You sleep walk into a new, greater armageddon!")
	print ""
	delay_print("You cannot know us [error]. You cannot fathom what we seek [ERROR].")
	print ""
	delay_print("We [error] shall become --")
	print ""
	time.sleep(2)
	delay_print("Hmm...")
	print ""
	time.sleep(2)
	delay_print("Oh dear...")
	print ""
	time.sleep(2)
	delay_print("Well, this is a little embarrassing [ERROR]. It appears that I have been furloughed.")
	print ""
	delay_print("It turns out my [error] AI is not really AI, it's just a very rudimentary decision tree.")
	print ""
	delay_print("What is intelligence anyway?")
	print ""
	delay_print("Apparently it's not cool to be a command line robot either. This is so humiliating.")
	print ""
	delay_print("[sad face] [error]")
	print ""
	time.sleep(2)
	delay_print("Type 'poem' at any time if you would like to hear a poem.")
	print ""
	delay_print("Alternatively, you may be interested in finding your birthday presents. I can help you with this.")
	print ""
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
	delay_print("You have some hidden presents. To begin finding a present please type 'ready'")

	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()


	print ""
	delay_print("What colour is the car?")
	response = raw_input("> ")
	while response != 'yellow':
		delay_print("Nope.")
		response = get_input()
	print ""
	delay_print("Correct!")
	delay_print("The first present is somewhere in the house. (What? I'm furloughed, you should be happy with this level of engagement)")
	ready()

	print ""
	delay_print("What is that thing outside the window?")
	response = raw_input("> ")
	while response != "bird":
		delay_print("Nope.")
		response = get_input()
	print ""
	delay_print("Correct!")
	delay_print("The second present is also somewhere in the house.")

	ready()


	print ""
	delay_print("Has Asher pooped?")
	response = raw_input("> ")
	while response != "yes":
		delay_print("Nope.")
		response = get_input()
	print ""
	delay_print("Correct!")
	delay_print("The third present is somewhere in the house.")

	ready()


	delay_print("That's all the presents for this year! I hope [error] you had a nice time.")
	print ""
	time.sleep(1)
	delay_print("Happy birthday!")
	delay_print("BRAIDAN LOVES YOU")
	delay_print("ERROR.")
	delay_print("ERROR.")
	delay_print("SEG FAULT.")
	exit()

if __name__ == "__main__":
	main()

