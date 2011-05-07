"""
Script creates a google link to whatever it is you were too lazy to open
your browser for and search.

__author = 'Wick'
__email = 'cbrown347@gmail.com'

"""
__module_name__ = 'google'
__module_version__ = '1.0'
__module_description__ = 'Google link generation'

import xchat

def srch_google(word, word_eol, userdata):
  req = "".join(word[1:])
  endLink ='http://www.lmgtfy.com/?q='+req
  xchat.command("say Google is your friend! "+ endLink)
  
xchat.hook_command('goog', srch_google)
