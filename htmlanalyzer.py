#!/usr/bin/python
#
# HTML source analyzer
#

def main():
    _file = open("index.html", "r")

    while (_line = _file.readline()):
        print _line
        
# main program
if __name__ == "__main__":
    main()
