#!/usr/bin/python

import email
import glob
import sys
import argparse

def processArguments():
    parser = argparse.ArgumentParser("Extract Mail attachments")
    parser.add_argument('-t', '--type', help='type to extract')
    parser.add_argument('-d', '--directory', help='directory')
    parser.add_argument('-o', '--output', help='destination folder')
    parser.add_argument('files', metavar='files', nargs='?', help="file to process")
    return vars(parser.parse_args())
    


def main():
#    args = processArguments()
#    print args
#    if args['files'
    if len(sys.argv) < 2:
        emails_list = glob.glob("*")
    else:
        emails_list = sys.argv[1:]
    for current_email in emails_list:
        print "# Processing %s" % current_email
        msg = email.message_from_file(open(current_email))
        payloads = msg.get_payload()
        print "# Content-type : %s" % msg.get_content_type()
        if msg.get_content_type() in ['text/plain', 'text/html']:
            continue
        print "# Number of payloads : %i" % len(payloads)
        for payload in payloads:
            print "# Type of payload %s" % payload.get_content_type()


main()

