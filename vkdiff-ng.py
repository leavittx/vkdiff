#!/usr/bin/python
# -*- coding: utf-8 -*-

from grab import Grab
import re, getopt, sys, os
import getpass
import ConfigParser
import codecs

email = '  '
password = '  '
path = ' '

HELPSTR = 'vkdiff by np3 & lp3, 2009-2010\nUsage:\n-g, --get   - Get friends from web and write them to database\n\
-d, --diff  - Diff friends from web and saved in database\n-p, --print - Print database\n\
-h, --help  - Display this help\n\
-n, --name  - Use own profile(not default)\n\
-a, --add   - Add own profile'

DATAFILE = 'database'
ACCFILE = 'accounts'
DEFSECTION = 'Def'

def help():
  print HELPSTR
  
def procinfo(list):
  newstr = ''
  for i in list:
    newstr += i[0] + ' ' + i[1] +  '\n'
  writefile(newstr[:-1], path)

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
      f = codecs.open(file, encoding='utf-8', mode='w')
      f.write(buf.decode('cp1251', 'replace'))
      f.close()
      
def readfile(file):
    try:
      f = open(file)
      return f.read()
    except IOError, err:
      print path + " : " + err.strerror
      sys.exit(0)
      
def printbase():
    print readfile(path)
    
def diff():
    R = []
    s1 = readfile(path)
    b1 = s1.split('\n')
    for i in b1:
     t = i.split(' ')
     try:
       R.append((t[0],t[1] + ' ' + t[2]))
     except IndexError:
       try:
         R.append((t[0],t[1]))
       except IndexError:
         print "Something wrong in database file"
         sys.exit(0)

    
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
 #     R.append(t[0])#!/usr/bin/python
# -*- coding: utf-8 -*-

from grab import Grab
import re, getopt, sys, os
import getpass
import ConfigParser
import codecs

email = '  '
password = '  '
path = ' '
HELPSTR = 'vkdiff by np3 & lp3, 2009-2010\nUsage:\n-g, --get   - Get friends from web and write them to database\n\
-d, --diff  - Diff friends from web and saved in database\n-p, --print - Print database\n\
-h, --help  - Display this help\n\
-n, --name  - Use own profile(not default)\n\
-a, --add   - Add own profile'

DATAFILE = 'database'
ACCFILE = 'accounts'
DEFSECTION = 'Def'

def help():
  print HELPSTR

def procinfo(list):
  newstr = ''
  for i in list:
    newstr += i[0] + ' ' + i[1] +  '\n'
  writefile(newstr[:-1], path)

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
      f = codecs.open(file, encoding='utf-8', mode='w')
      f.write(buf.decode('cp1251', 'replace'))
      f.close()

def readfile(file):
    try:
      f = open(file)
      return f.read()
    except IOError, err:
      print path + " : " + err.strerror
      sys.exit(0)

def printbase():
    print readfile(path)

def diff():
    R = []
    s1 = readfile(path)
    b1 = s1.split('\n')
    for i in b1:
     t = i.split(' ')
     try:
       R.append((t[0],t[1] + ' ' + t[2]))
     except IndexError:
       try:
         R.append((t[0],t[1]))
       except IndexError:
         print "Something wrong in database file"
         sys.exit(0)


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
        print '+ ' + b2[item].decode('cp1251', 'replace')

    for item in b1.keys():
      if not item in b2.keys():
        print '- ' + b1[item]
    l1 = len(b1)
    l2 = len(b2)
    if l1 == l2:
      print "Snapshots are equal!\nFriends: " + str(l1)
    else:
      print 'Friends\nOld: ' + str(l1) + '\nNew: ' + str(l2)
def add_account(name):
    if name == '':
      name = DEFSECTION
    config = ConfigParser.RawConfigParser()
    config.read(ACCFILE)
    try:
       email = config.get(name, 'Login')
       print "Already exists!"
       sys.exit(0)
    except ConfigParser.NoSectionError:
     print "Login:"
     login = str(raw_input())
    #Security fix
    #print "Password:"
    #pwd = str(raw_input())
     pwd = getpass.getpass()
     config = ConfigParser.RawConfigParser()
     config.add_section(name)
     config.set(name, 'Login', login)
     config.set(name, 'Password', pwd)
     with open(ACCFILE, 'ab') as configfile:
 	 config.write(configfile)
     os.mkdir(name)
     path = name + '/' + DATAFILE
     return (login, pwd, path)
def get_account(name):
  config = ConfigParser.RawConfigParser()
  config.read(ACCFILE)
  if name == '':
    name = DEFSECTION
  try:
    email = config.get(name, 'Login')
  except ConfigParser.NoSectionError as S:
    print "No account " + S.section
    sys.exit(0)
  password = config.get(name, 'Password')
  path = name + '/' + DATAFILE
  return (email, password, path)
if __name__ == "__main__":
    g = Grab()
    try:
      opts, args = getopt.getopt(sys.argv[1:], "n:a:phgd", ["name", "add", "print", "help", "get", "diff"])
    except getopt.GetoptError, err:
       print err
       help()
       sys.exit(0);
    if os.path.exists(ACCFILE) == False:
       #print "Login:"
       #login = str(raw_input())
       #Security fix
       #print "Password:"
       #pwd = str(raw_input())
       #pwd = getpass.getpass()
       #config = ConfigParser.RawConfigParser()
       #config.add_section('Account')
       #config.set('Account', 'Login', login)
       #config.set('Account', 'Password', pwd)
       #with open('account', 'wb') as configfile:
       #  config.write(configfile)
       (email, password, path) = add_account('')
    else:
       (email, password, path) = get_account('')
    if len(opts) == 0:
        diff()
        sys.exit(0)
    for o, a in opts:
	if o in ('-n', '--name'):
	    (email, password, path) = get_account(a)
	elif o in ('-a', '--add'):
            (email, password, path) = add_account(a)
        elif o in ('-h', '--help'):
            help()
        elif o in ('-g', '--get'):
            procinfo(get())
        elif o in ('-p', '--print'):
            printbase()
        elif o in ('-d', '--diff'):
            diff()
    sys.exit(0)

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
        print '+ ' + b2[item].decode('cp1251', 'replace')

    for item in b1.keys():
      if not item in b2.keys():
        print '- ' + b1[item]
    l1 = len(b1)
    l2 = len(b2)
    if l1 == l2:
      print "Snapshots are equal!\nFriends: " + str(l1) 
    else:
      print 'Friends\nOld: ' + str(l1) + '\nNew: ' + str(l2)
def add_account(name):
    if name == '':
      name = DEFSECTION
    config = ConfigParser.RawConfigParser()
    config.read(ACCFILE)
    try:
       email = config.get(name, 'Login')
       print "Already exists!"
       sys.exit(0)
    except ConfigParser.NoSectionError:
     print "Login:"
     login = str(raw_input())
    #Security fix
    #print "Password:"
    #pwd = str(raw_input())
     pwd = getpass.getpass()
     config = ConfigParser.RawConfigParser()
     config.add_section(name)
     config.set(name, 'Login', login)
     config.set(name, 'Password', pwd)
     with open(ACCFILE, 'ab') as configfile:
 	 config.write(configfile)
     os.mkdir(name)
     path = name + '/' + DATAFILE
     email = login
     password = pwd
     return (email, password, path)
def get_account(name):
  config = ConfigParser.RawConfigParser()
  config.read(ACCFILE)
  if name == '':
    name = DEFSECTION
  try:
    email = config.get(name, 'Login')
  except ConfigParser.NoSectionError as S:
    print "No account " + S.section
    sys.exit(0)  
  password = config.get(name, 'Password')
  path = name + '/' + DATAFILE
  return (email, password, path)
if __name__ == "__main__":
    g = Grab()
    try:
      opts, args = getopt.getopt(sys.argv[1:], "n:a:phgd", ["name", "add", "print", "help", "get", "diff"])
    except getopt.GetoptError, err:
       print err
       help()
       sys.exit(0);
    if os.path.exists(ACCFILE) == False:
       #print "Login:"
       #login = str(raw_input())
       #Security fix
       #print "Password:"
       #pwd = str(raw_input())
       #pwd = getpass.getpass()
       #config = ConfigParser.RawConfigParser()
       #config.add_section('Account')
       #config.set('Account', 'Login', login)
       #config.set('Account', 'Password', pwd)
       #with open('account', 'wb') as configfile:
       #  config.write(configfile)
       (email, password, path) = add_account('')
    else:
       (email, password, path) = get_account('')
    if len(opts) == 0:
        diff()
        sys.exit(0)
    for o, a in opts:
	if o in ('-n', '--name'):
	    (email, password, path) = get_account(a)
	elif o in ('-a', '--add'):
            (email, password, path) = add_account(a)
        elif o in ('-h', '--help'):
            help()
        elif o in ('-g', '--get'):
            procinfo(get())
        elif o in ('-p', '--print'):
            printbase()
        elif o in ('-d', '--diff'):
            diff()
    sys.exit(0)
