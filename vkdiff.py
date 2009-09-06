
#!/usr/bin/python
# -*- coding: utf-8 -*-

from grab import Grab
import re, getopt, sys, os

HELPSTR = '-p, --print - Print current database\n-h, --help - Print this message\n-g, --grep - Grep friends\n-d, --diff - Find the difference'
DATAFILE = 'database'
def help():
  print HELPSTR
def grep():
  g.setup(url='http://pda.vkontakte.ru/login',
                    post={'email' : 'george15@list.ru', 'pass' : 'coldplay15'})
  g.request()
  g.setup(url='http://pda.vkontakte.ru/write')
  g.request()
  list = re.findall('<option value\="([0-9]+)" >',g.response_body)
  return list

def writefile(buf, file):
  
    if os.path.exists(file):
      f = open(file, 'rw+')
      data = f.read()
      data += buf
      f.seek(0,0)
      f.write(data)
      f.truncate(f.tell())
      f.close()
    else:
      f = open(file, 'w')
      f.write(buf)
      f.close()
def readfile(file):
    try:
      f = open(file)
      return f.read()
    except IOError, err:
      print err.strerror
     
   

def printbase():
    print readfile(DATAFILE)
def diff():
    s1 = readfile(DATAFILE)
    b1 = s1.split('\n')
    b2 = grep()
    length = len(b1) - 1
    len2 = len(b2)
    
    if len2 <= length:
      for i in range(0, len2 ):
        if b1[i] != b2[i]:
          print "DIFF - " + b1[i] + ' ' + b2[i]
      i += 1
      for i in range(i, length ):
            print "DIFF - " + b1[i] + ' ' + '(Empty)'

    if len2 > length:
        for i in range(0, length ):
          if b1[i] != b2[i]:
            print "DIFF - " + b1[i] + ' ' + b2[i]
        i += 1
        for i in range(i, len2 ):
            print "DIFF - (Empty) " + b2[i]

if __name__ == "__main__":
    g = Grab()
    newstr = ''
    try:
      opts, args = getopt.getopt(sys.argv[1:], "phgd", ["print", "help", "grep", "diff"])
    except getopt.GetoptError, err:
       print err
       help()
       sys.exit(0);
    if len(opts) == 0:
        help()
        sys.exit()
    for o, a in opts:
        if o in ('-h', '--help'):
            help()
            sys.exit()
        elif o in ('-g', '--grep'):
            l = grep()
            
            for s in l:
                newstr += s + '\n'
            
            writefile(newstr, DATAFILE)
        elif o in ('-p', '--print'):
            printbase()
            sys.exit()
        elif o in ('-d', '--diff'):
            diff()
            sys.exit()
       
