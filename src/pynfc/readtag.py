import nfc
import ndef

def connected(tag):
	print(tag)
	print(tag.ndef.message.pretty() if tag.ndef else "Sorry, no NDEF")
	return False
	
#device = 'tty:S1'
device = 'tty:AMA0'

with nfc.ContactlessFrontend(device) as clf:
	clf.connect(rdwr={'on-connect': connected})
