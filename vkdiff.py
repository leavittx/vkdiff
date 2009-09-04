
#!/usr/bin/python
# -*- coding: utf-8 -*-

from grab import Grab
import re

g = Grab()
g.setup(url='http://vkontakte.ru/login.php',
        post={'email' : '', 'pass' : ''})
g.request()
g.setup(url='http://vkontakte.ru' + g.headers['Location'])
g.request()
g.setup(url='http://vkontakte.ru/friends.php')
g.request()
#list = re.findall(u'[0-9]{4,},"[А-Яа-яA-Za-z0-9]{10,}"',g.response_body)
list = re.findall(u'[0-9]{4,},"',g.response_body)
print list
print len(list)
