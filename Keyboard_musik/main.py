from __future__ import print_function
import time
from playsound import playsound
from inputs import get_key

def main():
	print("started")
	sd=-1
	prev=-1
	while 1:
		events = get_key()
		if events:
			for event in events:
				print(event.ev_type, event.code, event.state)
				sd=event.state
				print(sd)
				break
			print(prev, sd)
			if prev!=sd:
				playsound('notes/sound ('+str(sd)+').wav')
				prev=sd


if __name__ == "__main__":
	main()