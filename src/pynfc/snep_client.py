import nfc
import nfc.snep
import ndef

def startup(llc):
    print("Startup")
    global snep_client
    snep_client = nfc.snep.SnepClient(llc)
    return llc

def connected(llc):
    print("Connected")
    socket = nfc.llcp.Socket(llc, nfc.llcp.DATA_LINK_CONNECTION)
    socket.connect('urn:nfc:sn:snep')
    records = [ndef.UriRecord("http://nfcpy.org")]
    message = b''.join(ndef.message_encoder(records))
    socket.send(b"\x10\x02\x00\x00\x00" + chr(len(message)) + message)
    print(socket.recv())
    socket.close()
    #global snep_client
    #snep_client.put_records([ndef.UriRecord("http://nfcpy.org")])
    return True

snep_client = None
clf = nfc.ContactlessFrontend("tty:S1")
clf.connect(llcp={'on-startup': startup, 'on-connect': connected})



