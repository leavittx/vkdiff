
#!/usr/bin/python
# -*- coding: utf-8 -*-

from grab import Grab
import re

g = Grab()
g.setup(url='http://pda.vkontakte.ru/login',
        post={'email' : 'george15@list.ru', 'pass' : 'coldplay15'})
g.request()
g.setup(url='http://pda.vkontakte.ru/write')
g.request()
list = re.findall('<option value\="([0-9]+)" >',g.response_body)
print list
print len(list)
