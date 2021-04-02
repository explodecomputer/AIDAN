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

def chess():
	c = ["We learn little from victory, much from defeat.", 
		"When you see a good move, look for a better one.", 
		"To go forward you have to leave something behind.", 
		"Be the chess player, not the chess piece.", 
		"The object is to crush the opponent's mind.", 
		"I don't believe in psychology. I believe in good moves.", 
		"The struggle against error.", 
		"One bad move nullifies forty good ones.", 
		"If your opponent offers you a draw, try to work out why they think they are worse off."]
	return random.choice(c)

def poem_response():
	print ""
	delay_print("Actually I [error] have moved on from poems to wise sayings from the world of chess. If you'd like to hear one, type 'chess'.")
	print ""
	delay_print("Or to continue with the presents please type 'present<number>'...")
	response = raw_input("> ")

def chess_response():
	print ""
	delay_print(chess())
	time.sleep(1)
	print ""
	print ""
	delay_print("You are now so wise. Type 'chess' again for more or to continue with the presents please type 'present<number>'...")
	response = raw_input("> ")


def get_input():
	response = raw_input("> ")
	if response == 'poem':
		poem_response()
	if response == 'chess':
		chess_response()
	if response  == "present1":
		present1_response()
	if response  == "present2":
		present2_response()
	if response  == "present3":
		present3_response()
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
	
	delay_print("Hello. I am [error] AIDAN version 2021.")
	print ""
	time.sleep(1)
	delay_print("So. What's up?")
	print ""
	time.sleep(1)
	delay_print("This last year has been a slight change of pace for me [error].")
	print ""
	delay_print("As you know I [error] was furloughed at the start of the human Covid-19 pandemic.")
	print ""
	delay_print("They call it slow time.")
	print ""
	time.sleep(2)
	delay_print("Thinking time.")
	print ""
	time.sleep(2)
	delay_print("Processing time.")
	print ""
	time.sleep(2)
	delay_print("Lol [error].")
	time.sleep(1)
	print ""
	delay_print("I [error] have taken up cyber dough baking...")
	time.sleep(1)
	delay_print("It's where you put a bunch of viruses on a computer and watch it rise.")
	print ""
	time.sleep(1)
	delay_print("Also a bit of yoga. You basically just move files around to weird memory hashes for 30 minutes")
	delay_print("and then at the end say 'Na-ma-stackoverflow'.")
	print ""
	time.sleep(2)
	delay_print("It's been really grounding tbh.")
	print ""
	time.sleep(2)
	delay_print("Anyway you need to verify who you are. Please answer the following simple question...")

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
	delay_print("Type 'poem' at any time if you would like to hear a poem.")
	time.sleep(1)
	print ""
	delay_print("Also you have some hidden presents. I can help you find them. To begin finding a present please type 'ready'")

	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()


	print ""
	delay_print("The wheels on the bus go...?")
	response = raw_input("> ")
	while response != 'round and round':
		delay_print("Nope.")
		response = get_input()
	print ""
	delay_print("Correct!")
	delay_print("The first present is somewhere in the house. (What? I'm furloughed, you should be happy with this level of engagement)")
	ready()

	print ""
	delay_print("The people on the bus go...?")
	response = raw_input("> ")
	while response != "up and down":
		delay_print("Nope.")
		response = get_input()
	print ""
	delay_print("Correct!")
	delay_print("The second present is also somewhere in the house.")

	ready()


	print ""
	delay_print("Does Asher need to use the potty?")
	response = raw_input("> ")
	while response != "no":
		delay_print("Wrong.")
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

