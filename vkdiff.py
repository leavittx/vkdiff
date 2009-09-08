#!/usr/bin/python
# -*- coding: utf-8 -*-

from grab import Grab
import re, getopt, sys, os

#insert your account info below =)
email = ''
password = ''

HELPSTR = 'vkdiff by np3 & lp3, 2009\nUsage:\n-g, --get   - Get friends from web and write them to database\n\
-d, --diff  - Diff friends from web and saved in database\n-p, --print - Print database\n\
-h, --help  - Display this help'

DATAFILE = 'database'

def help():
  print HELPSTR
  
def get():
#!!!
  #g.setup(url='http://vkontakte.ru/login.php', post={'email' : email, 'pass' : password}) 
  g.setup(url='http://pda.vkontakte.ru/login', post={'email' : email, 'pass' : password})
#!!!
  g.request()
#!!!
  #g.setup(url='http://vkontakte.ru/friends.php')
  g.setup(url='http://pda.vkontakte.ru/write')
#!!!
  g.request()
  #udata = unicode(g.response_body).decode('utf-8')
#!!!
  #list = re.findall('\[(\d+),"([^"]*)', g.response_body)
  list = re.findall('<option value\="([0-9]+)" >', g.response_body)
#!!!
  #print list
  return list
  
def writefile(buf, file):
  
#    if os.path.exists(file):
# hmm...why? try to update the database twice or more
# some fix is needed
#      f = open(file, 'rw+')
#      data = f.read()
#      data += buf
#      f.seek(0,0)
#      f.write(data)
#      f.truncate(f.tell())
#      f.close()
#    else:
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
    b2 = get()
    
#    length = len(b1) - 1
#    len2 = len(b2)
    
#    if len2 <= length:
#      for i in range(0, len2 ):
#        if b1[i] != b2[i]:
#          print "DIFF - " + b1[i] + ' ' + b2[i]
#      i += 1
#      for i in range(i, length ):
#            print "DIFF - " + b1[i] + ' ' + '(Empty)'

#   if len2 > length:
#        for i in range(0, length ):
#          if b1[i] != b2[i]:
#            print "DIFF - " + b1[i] + ' ' + b2[i]
#        i += 1
#        for i in range(i, len2 ):
#            print "DIFF - (Empty) " + b2[i]

    for item in b1:
      if not item in b2:
        print '- ' + item

    for item in b2:
      if not item in b1:
        print '+ ' + item

if __name__ == "__main__":
    g = Grab()
    newstr = ''
    try:
      opts, args = getopt.getopt(sys.argv[1:], "phgd", ["print", "help", "get", "diff"])
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
        elif o in ('-g', '--get'):
#!!!            L = []
            l = get()
#!!!            print l
#            for i in l:
#              L[:] = i[:]
#              for j in L:
#                print j.decode('utf-8')
           # l[0][0].decode('utf-8') 
            for s in l: #!!!
                newstr += s + '\n' #!!!
            
            writefile(newstr[:-1], DATAFILE) #!!!
        elif o in ('-p', '--print'):
            printbase()
            sys.exit()
        elif o in ('-d', '--diff'):
            diff()
            sys.exit()
