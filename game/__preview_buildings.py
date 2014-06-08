#!/usr/bin/python

#import sys

from _research_areas import RESEARCH_AREAS
from _tech_table import TECH_TABLE
from _buildings import BUILDINGS


def main():
    """
        MAIN
    """
    for b_id in BUILDINGS:
        if b_id:
            b = BUILDINGS[b_id]
            if b['tech']:
                    tech_name = TECH_TABLE[b['tech']]['name']
                    if TECH_TABLE[b['tech']]['area']:
                        area_name = RESEARCH_AREAS[TECH_TABLE[b['tech']]['area']]['name']
            else:
                    tech_name = "???"
                    area_name = "???"
            print("%s : %s ... %s @ %s" % (str(b_id).rjust(3), b['name'].ljust(20), tech_name.ljust(30), area_name))

if __name__ == "__main__":
    main()
