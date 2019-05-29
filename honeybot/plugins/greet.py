# -*- coding: utf-8 -*-
"""
[greet.py]
Greet Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
responds to .hi, demo of a basic plugin

[Commands]
>>> .hi
returns hoo
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            try:
                msgs = info['args'][1:][0].split()
            except Exception as e:
                pass
            if info['command'] == 'PRIVMSG' and msgs[0] == '.hi':
                methods['send'](info['address'], 'hooo')
        except Exception as e:
            print('woops plug', e)
