import nfc
import ndef

def connected(tag):
	print(tag)
	print(tag.ndef.message.pretty() if tag.ndef else "Sorry, no NDEF")
	return False

with nfc.ContactlessFrontend('tty:S1') as clf:
	clf.connect(rdwr={'on-connect': connected})