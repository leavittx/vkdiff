#!/usr/bin/python
# -*- coding: utf-8 -*-

from grab import Grab
import re, getopt, sys, os

#insert your account info below =)
email = 'itmodermo@mail.ru'
password = 'linuxa'

HELPSTR = 'vkdiff by np3 & lp3, 2009\nUsage:\n-g, --get   - Get friends from web and write them to database\n\
-d, --diff  - Diff friends from web and saved in database\n-p, --print - Print database\n\
-h, --help  - Display this help'

DATAFILE = 'database'

def help():
  print HELPSTR
  
def get():
#!!!
  g.setup(url='http://vkontakte.ru/login.php', post={'email' : email, 'pass' : password}) 
  #g.setup(url='http://pda.vkontakte.ru/login', post={'email' : email, 'pass' : password})
#!!!
  g.request()
#!!!
  g.setup(url='http://vkontakte.ru/friends.php')
  #g.setup(url='http://pda.vkontakte.ru/write')
#!!!
  g.request()
  #udata = unicode(g.response_body).decode('utf-8')
#!!!
  list = re.findall(u'\[(\d+),"([^"]*)', g.response_body)
  #list = re.findall('<option value\="([0-9]+)" >', g.response_body)
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
      f.write(buf.encode('utf-8'))
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
    R = []
    s1 = readfile(DATAFILE)
    b1 = s1.split('\n')
    for i in b1:
     t = i.split(' ')
     try:
       R.append((t[0],t[1] + ' ' + t[2]))
     except IndexError:
       R.append((t[0],t[1]))
    
    b1 = dict(R)
    b2 = dict(get())

    

    if len(b2) == 0:
        print "Bad response from vkontakte.ru"
        sys.exit(0)
   # print b1.keys()
   # print b2.keys()
   #
  #  print b2
  #for i in b2:
  #    L.append((i[0], i[1]))
   # print L
    #b1[:] = b1[:-1]
 #   for i in b1:
 #     t = i.split(' ')
 #     R.append(t[0])
    #print R
    #sys.exit(0)
    
    
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

    for item in b2.keys():
      if not item in b1.keys():
        print '+ ' + b2[item]

    for item in b1.keys():
      if not item in b2.keys():
        print '- ' + b1[item]
     
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
       # help()
        diff()
        sys.exit()
    for o, a in opts:
        if o in ('-h', '--help'):
            help()
            sys.exit()
        elif o in ('-g', '--get'):
            l = get()
            for i in l:
              newstr += i[0] + ' ' + i[1] +  '\n'
     
            writefile(newstr[:-1], DATAFILE) #!!!
        elif o in ('-p', '--print'):
            printbase()
            sys.exit()
        elif o in ('-d', '--diff'):
            diff()
            sys.exit()
