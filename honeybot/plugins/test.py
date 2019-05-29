# -*- coding: utf-8 -*-
"""
[test.py]
Test Plugin

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
tests run
"""


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        # if '!~' in info['prefix']:
            # print(info)
        try:
            try:
                msgs = info['args'][1:][0].split()
            except Exception as e:
                pass
            if info['command'] == 'PRIVMSG' and msgs[0] == '.test':
                methods['send'](info['address'], 'test ok')
        except Exception as e:
            print('woops plug', e)
