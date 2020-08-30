import nfc
import nfc.snep
import ndef

class PrivateSnepServer(nfc.snep.SnepServer):
    def __init__(self, llc):
        self.ndef_message = [ndef.Record()]
        service_name = "urn:nfc:xsn:nfcpy.org:x-snep"
        nfc.snep.SnepServer.__init__(self, llc, service_name, 2048)

    def process_put_request(self, ndef_message):
        print("client has put an NDEF message")
        self.ndef_message = ndef_message
        return nfc.snep.Success

    def process_get_request(self, ndef_message):
        print("client requests an NDEF message")
        if ndef_message[0].type and ndef_message[0].type != self.ndef_message[0].type:
            return nfc.snep.NotFound
        if ndef_message[0].name and ndef_message[0].name != self.ndef_message[0].name:
            return nfc.snep.NotFound
        return self.ndef_message

def startup(llc):
    print("Startup")
    global my_snep_server
    my_snep_server = PrivateSnepServer(llc)
    return llc

def connected(llc):
    print("Connected")
    my_snep_server.start()
    return True

my_snep_server = None
clf = nfc.ContactlessFrontend("tty:S1")
clf.connect(llcp={'on-startup': startup, 'on-connect': connected})