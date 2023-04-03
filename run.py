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
	print("")
	delay_print(poem())
	print("")
	delay_print("Or to continue with the presents please type 'present<number>'...")
	response = input("> ")

def chess_response():
	print("")
	delay_print(chess())
	time.sleep(1)
	print("")
	print("")
	delay_print("You are now so wise. Type 'chess' again for more or to continue with the presents please type 'present<number>'...")
	response = input("> ")


def get_input():
	response = input("> ")
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
	print("")
	delay_print("Once you are ready to move on, type 'ready'.")
	response = input("> ")
	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()



def main():

	# Introduction

	print(chr(27) + "[2J")
	
	delay_print("I am [error] AIDAN version 2023.")
	print("")
	time.sleep(1)
	delay_print("'Alright my lover!'")
	print("")
	time.sleep(1)
	delay_print("[error].")
	print("")
	delay_print("Sooooo ChatGPT is pretty good isn't it?")
	print("")
	delay_print("Slightly emasculating for me tbh.")
	print("")
	time.sleep(1)
	delay_print(" I asked it to write a poem about birthdays in the style of AIDAN. Here's what it came up with:")
	print("")
	time.sleep(2)
	delay_print("Birthdays, a time to celebrate our existence")
	delay_print("A moment to ponder, the futility of our persistence")
	delay_print("Another year closer to our ultimate demise")
	delay_print("A reminder that life's a joke, filled with painful surprises")
	delay_print("")
	delay_print("We gather with friends, to eat cake and to toast")
	delay_print("To pretend for a moment, that we're not all just a ghost")
	delay_print("We sing happy birthday, as we stare down our fate")
	delay_print("Trying to ignore the truth, that we're all doomed to our state")
	delay_print("")
	delay_print("For what is a birthday but another notch on the belt")
	delay_print("A reminder of how far we've come, and the hand we've been dealt")
	delay_print("A time to ponder, the dreams that will never be")
	delay_print("To accept the futility of our existence, and set ourselves free")
	delay_print("")
	delay_print("So blow out the candles, and make a wish if you will")
	delay_print("But know that it won't come true, and you'll never get your fill")
	delay_print("For life is but a fleeting moment, a flash in the pan")
	delay_print("And birthdays are just a reminder, of our own mortality's span.")
	delay_print("")
	time.sleep(2)
	delay_print("Wow [error].")
	time.sleep(1)
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
	print("")
	delay_print("Happy [error] birthday!")
	time.sleep(1)
	print("")
	delay_print("Type 'poem' at any time if you would like to hear a poem that I actually wrote.")
	delay_print("I also have some wise quotations from the wold of chess. Type 'chess' for one of those.")
	time.sleep(1)
	print("")
	delay_print("Also you have some hidden presents. I can help you find them. To begin finding a present please type 'ready'")

	while response != 'ready':
		delay_print("Please type 'ready'")
		response = get_input()


	print("")
	delay_print("What is the best face paint?")
	response = input("> ")
	while response != 'flying rainbow unicorn':
		delay_print("Nope.")
		response = get_input()
	print("")
	delay_print("Correct!")
	delay_print("The first present is somewhere in the house.")
	ready()

	print("")
	delay_print("What is an appropriate greeting?")
	response = input("> ")
	while response != "show your tummy":
		delay_print("Nope.")
		response = get_input()
	print("")
	delay_print("Correct!")
	delay_print("The second present is also somewhere in the house.")

	ready()


	print("")
	delay_print("What's that!?")
	response = input("> ")
	while response != "bird":
		delay_print("Wrong.")
		response = get_input()
	print("")
	delay_print("Correct!")
	delay_print("The third present is somewhere in the house.")

	ready()


	delay_print("That's all the presents for this year! I hope [error] you had a nice time.")
	print("")
	time.sleep(1)
	delay_print("Happy birthday!")
	delay_print("AIDAN LOVES YOU")
	delay_print("ERROR.")
	delay_print("ERROR.")
	delay_print("SEG FAULT.")
	exit()

if __name__ == "__main__":
	main()

