#!/usr/bin/python

import sys

from _research import RESEARCH_AREAS
from _tech_table import TECH_TABLE

def preview_area(area):
    while area:
	techs = ""
	for tech_id in TECH_TABLE:
	    tech = TECH_TABLE[tech_id]
	    if tech['area'] == area:
#		techs.append(tech['name'])
		techs += "%s : %s" % (str(tech_id).rjust(3), tech['name'].ljust(30))
#	print(" * %s" % techs)
#	print("" % (RESEARCH_AREAS[area]['name'], techs))
        print("%2i : %s (%s RP) :   %s " % (area, RESEARCH_AREAS[area]['name'].rjust(30), str(RESEARCH_AREAS[area]['cost']).rjust(5), techs))
	area = RESEARCH_AREAS[area]['next']
    print("")


def main(argv):
    """
        MAIN
    """
#    argc = len(argv)
#    if argc < 2:
#        print("Usage: %s <research_area>" % argv[0])
#        sys.exit(1)

#    area = int(argv[1])
    preview_area(4)
    preview_area(55)

    preview_area(22)
    preview_area(10)

    preview_area(28)
    preview_area(18)

    preview_area(57)
    preview_area(7)

if __name__ == "__main__":
    main(sys.argv)
