from __future__ import print_function
import time
import sys
import pygame.midi
from inputs import get_key

def main():
	pygame.midi.init()
	player = pygame.midi.Output(0)
	player.set_instrument(0)
	print("started")
	sd=-1
	prev=-1
	t0=0
	while 1:
		events = get_key()
		if events:
			for event in events:
				sd=event.state
				break
			print(prev, sd)
		if prev==sd:
			if t0==0:
				t0=time.time()
		else:
			t1=time.time()
			player.note_on(prev+36, 127)
			if t0==0:
				t0=t1-0.1
			print(t1-t0)
			time.sleep(t1-t0)
			player.note_off(prev+36, 127)
			prev=sd
			t0=0


if __name__ == "__main__":
	main() 
