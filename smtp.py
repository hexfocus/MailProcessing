import time
import smtpd
import asyncore

import os
import time
import string
import random


RANDOMSTRING = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
MAILDIR = os.getcwd() + "/MAILDIR-" + RANDOMSTRING

class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message length        :', len(data)

        for rcpt in rcpttos:
            (username, domain) = rcpt.split('@')
            destination_name = str(time.time())
            filename = "%s/%s/%s/%s" % (MAILDIR,
                                        domain,
                                        username,
                                        destination_name)
            try:
                os.makedirs(os.path.dirname(filename))
            except:
                pass
            fd = open(filename, "w")
            fd.write(data)
            fd.close()
    

    

server = CustomSMTPServer(('0.0.0.0', 25), None)

asyncore.loop()
