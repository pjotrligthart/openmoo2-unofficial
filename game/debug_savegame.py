#!/usr/bin/python

import sys
import os

from stat import ST_MTIME
from time import sleep
#import savegame
import moo2

def debug_research(data):
    PLAYER_0    = data['players'][0]

    research_item = PLAYER_0['research_item']
    research_progress = PLAYER_0['research_progress']
    research_area = PLAYER_0['research_area']

    print("")
    print("=== Player #0: === ")

    print("known_techs: %s" % PLAYER_0['known_techs'])

    print("research_area: %i" % research_area)
    print("research_progress: %i" % research_progress)
    print("research_item: %i" % research_item)
    print("")

    print("    %s:    {" % str(research_item).rjust(3))
    print("        'name':     \"\",")
    print("        'area':     %i," % research_area)
    print("    },")
    print("")


    print("=== /Player #0 ===")
    print("")
    
def debug_player0_unknown(savegame):
    player = savegame.parse_players()[0]
    print("")
    print("=== Player #0: === ")
    print("0x28: %i" % player['0x28'])
    print("0x29: %i" % player['0x29'])
    print("0x2A: %i" % player['0x2A'])
    print("0x2B: %i" % player['0x2B'])
    print("0x2C: %i" % player['0x2C'])
    print("0x2D: %i" % player['0x2D'])
    print("0x2E: %i" % player['0x2E'])
    print("0x2F: %i" % player['0x2F'])

    print("")

    print("0x40: %i ... %i ... %i ...%i" % (player['0x40'], player['0x41'], player['0x42'], player['0x43']))
    print("0x44: %i ... %i ... %i ...%i" % (player['0x44'], player['0x45'], player['0x46'], player['0x47']))
    print("0x48: %i ... %i ... %i ...%i" % (player['0x48'], player['0x47'], player['0x4A'], player['0x4B']))
    print("0x4C: %i ... %i ... %i ...%i" % (player['0x4C'], player['0x4D'], player['0x4E'], player['0x4F']))
#    , player['0x44'], player['0x45'], player['0x46'], player['0x47'], player['0x48'])
#    print("0x49: %i" % player['0x49'], player['0x4A'], player['0x4B'], player['0x4C'], player['0x4D'], player['0x4E'], player['0x4F'])
    
    print("")

    print("0x50: %i ... %i ... %i ...%i" % (player['0x50'], player['0x51'], player['0x52'], player['0x53']))
    print("0x54: %i ... %i ... %i ...%i" % (player['0x54'], player['0x55'], player['0x56'], player['0x57']))
    print("0x58: %i ... %i ... %i ...%i" % (player['0x58'], player['0x57'], player['0x5A'], player['0x5B']))
    print("0x5C: %i ... %i ... %i ...%i" % (player['0x5C'], player['0x5D'], player['0x5E'], player['0x5F']))

    print("")

    print("0x60: %i ... %i ... %i ...%i" % (player['0x60'], player['0x61'], player['0x62'], player['0x63']))
    print("0x64: %i ... %i ... %i ...%i" % (player['0x64'], player['0x65'], player['0x66'], player['0x67']))
    print("0x68: %i ... %i ... %i ...%i" % (player['0x68'], player['0x67'], player['0x6A'], player['0x6B']))
    print("0x6C: %i ... %i ... %i ...%i" % (player['0x6C'], player['0x6D'], player['0x6E'], player['0x6F']))

    print("")

    print("0x70: %i ... %i ... %i ...%i" % (player['0x70'], player['0x71'], player['0x72'], player['0x73']))
    print("0x74: %i ... %i ... %i ...%i" % (player['0x74'], player['0x75'], player['0x76'], player['0x77']))
    print("0x78: %i ... %i ... %i ...%i" % (player['0x78'], player['0x77'], player['0x7A'], player['0x7B']))
    print("0x7C: %i ... %i ... %i ...%i" % (player['0x7C'], player['0x7D'], player['0x7E'], player['0x7F']))

    print("")

    print("0x80: %i ... %i ... %i ...%i" % (player['0x80'], player['0x81'], player['0x82'], player['0x83']))
    print("0x84: %i ... %i ... %i ...%i" % (player['0x84'], player['0x85'], player['0x86'], player['0x87']))
    print("0x88: %i ... %i ... %i ...%i" % (player['0x88'], player['0x87'], player['0x8A'], player['0x8B']))
    print("0x8C: %i ... %i ... %i ...%i" % (player['0x8C'], player['0x8D'], player['0x8E'], player['0x8F']))

    print("")

    print("0x90: %i ... %i ... %i ...%i" % (player['0x90'], player['0x91'], player['0x92'], player['0x93']))
    print("0x94: %i ... %i ... %i ...%i" % (player['0x94'], player['0x95'], player['0x96'], player['0x97']))
    print("0x98: %i ... %i ... %i ...%i" % (player['0x98'], player['0x97'], player['0x9A'], player['0x9B']))
    print("0x9C: %i ... %i ... %i ...%i" % (player['0x9C'], player['0x9D'], player['0x9E'], player['0x9F']))

    print("")

    print("0xA0: %i" % player['0xA0'])
    print("0xA1: %i" % player['0xA1'])
    print("0xA2: %i" % player['0xA2'])
    print("0xA3: %i" % player['0xA3'])
    print("0xA4: %i" % player['0xA4'])
    print("0xA5: %i" % player['0xA5'])
    print("0xA6: %i" % player['0xA6'])
    print("0xA7: %i" % player['0xA7'])
    print("0xA8: %i" % player['0xA8'])

    print("")

    print("0xAD: %i" % player['0xAE'])
    print("0xAE: %i" % player['0xAE'])

    print("")
    print("research_progress: %i" % player['research_progress'])
    print("research_area: %i" % player['research_area'])
   

def main(argv):
    """
        MAIN
    """
    argc = len(argv)
    if argc < 2:
        print("Usage: %s <savegame>" % argv[0])
        sys.exit(1)

    filename = "../moo2/%s" % argv[1]


    mtime1 = 0
    while 1:
        st = os.stat(filename)
        mtime2 = st[ST_MTIME]
        if mtime1 != mtime2:
            print("mtime: %i" % mtime2)
            GAME = moo2.Moo2Savegame(filename)
            debug_player0_unknown(GAME)
            mtime1 = mtime2
        else:
            sleep(1)





if __name__ == "__main__":
    main(sys.argv)

