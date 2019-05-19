# -*- coding: utf-8 -*-
"""
[poker.py]
Poker Plugin

[Author]
Angelo Giacco

[About]
Play poker on honeybot

[Commands]
>>> .poker <command> <argument>
executes the command in the poker game
"""

from poker_assets import *

class Plugin():

    starting_chips = 100
    player_lst = []
    game_over = False
    winner = ""
    turn = 0
    game_created = False
    game_started = False

    def __init__(self):
        pass

    """
    USEFUL FUNCTIONS
    """

    def next_turn():
        '''increment turn and set to start if will cause index error'''
        try:
            Plugin.turn += 1
            if Plugin.turn == len(Plugin.player_lst):
                Plugin.turn -= len(Plugin.player_lst)
        except Exception as e:
            print("woops, poker turn change error ",e)

    """
    PLUGIN COMMANDS
    """

    def initGame(self,methods,info):
        '''create a new round'''

        if not Plugin.game_created:
            Plugin.player_lst = []
            name = info["prefix"].split("!")[0]
            Plugin.initPlayer(methods,info)
            Plugin.game_created = True
            Plugin.game_started = False
            DECK = deck.Deck()
            BOARD = board.Board(DECK.make_board())
            POT = pot.Pot()
            methods["send"](info["address"],name+" has started a round of poker! Use .poker join to join in!")
        else:
            methods["send"](info["address"],"A game already exists!")

    def initPlayer(self,methods,info):
        '''add a player to the round'''

        name = info["prefix"].split("!")[0]
        if len(Plugin.player_lst) <= 5:
            Plugin.player_lst.append(player.Player(len(Plugin.player_lst),Plugin.starting_chips,name))

        else:
            methods["send"](info["address"],"This round is full already")

    def start(self,methods,info):
        '''start the game'''
        Plugin.game_started = True
        Plugin.game_created = True
        for player in Plugin.player_lst:
            player.add_hand(hand.Hand(DECK.make_hand()))
            #should send each user their hand
        methods["send"](info["address"],"Here is the board of the game: "+BOARD.show_board())

    """
    RUNNING PLUGIN
    """

    def run(self, incoming, methods, info, bot_info):
        msgs = info['args'][1:][0].split()
        if msgs[0] == ".poker":
            if msgs[1] == "create":
                Plugin.initGame(methods,info)
            elif msgs[1] == "join":
                Plugin.initPlayer(methods,info)
            elif msgs[1] == "start":
                Plugin.start(methods,info)
