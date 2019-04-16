import cryFunc

import sys, getopt

def main(argv):
    if cryFunc.cryDetection(argv[0]) == 1:
        print "cry"
    else:
        print "non-cry"

if __name__ == "__main__":
   main(sys.argv[1:])
