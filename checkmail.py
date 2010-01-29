#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright (C) 2009, 2010 Markus Koch
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import poplib

class Account:

  NumMessages = 0

  def __init__(self, server, user, pass_, ssl):
    self.server = server
    self.user = user
    self.pass_ = pass_
    self.ssl = ssl

  def check(self):
    if self.ssl == True:
      Conn = poplib.POP3_SSL(self.server)
    else:
      Conn = poplib.POP3(self.server)
    
    Conn.user(self.user)
    Conn.pass_(self.pass_)
    Account.NumMessages += len(Conn.list()[1])
    Conn.quit()

Accounts = (
  Account('pop.example.org', 'alice@example.org', 'secret', True),
  Account('pop.example.com', 'bob', 'password', False),
  Account('pop.example.net', 'mallory@example.net', 'foobar', True),
)

for a in Accounts:
  try:
    a.check()
  except:
    print 'Hey, something went wrong!'
    

if Account.NumMessages > 0:
  if Account.NumMessages == 1:
    print 'Hey, you have got 1 new mail.' 
  else:
    print 'Hey, you have got ' + str(Account.NumMessages) + ' new mails.'
