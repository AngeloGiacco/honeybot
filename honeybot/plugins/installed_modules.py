# -*- coding: utf-8 -*-
"""
[installed_module.py]
Installation checker

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
checks if all listed in requirements.txt installed

[Commands]
>>> .installed
"""
#not showing
import importlib

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
            if info['command'] == 'PRIVMSG' and msgs[0] == '.installed':
                reqs = bot_info['required_modules']
                not_found = []
                for module in reqs:
                    try:
                        importlib.import_module(module)
                    except ModuleNotFoundError as e:
                        print('not found:', module)
                        not_found.append(module)
                if not_found:
                    methods['send'](info['address'], 'not found:{}'.format('-'.join(not_found)))
                else:
                    methods['send'](info['address'], 'all required modules installed')
        except Exception as e:
            print('woops plug', e)
