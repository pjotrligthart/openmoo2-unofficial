#!/usr/bin/env python

__author__="peterman"
__date__ ="$Jan 10, 2009 11:23:18 PM$"

from lbx import *
import savegame
import dictionary

DICTIONARY = dictionary.get_dictionary()


xDICTIONARY = {
    'COLONY_TYPES':             ["Colony", "Outpost"],

    'RACE_PICTURES ':           ["Alkari", "Bulrathi", "Darlok", "Elerian", "Gnolam", "Human", "Klackon", "Meklar", "Mrrshan", "Psilon", "Sakkra", "Silicoid", "Trilarian"],

    'PLANET_TYPES':             ['?', 'Asteroids', 'Gas Giant', 'Planet', '??', '???', '????', '?????'],
    'PLANET_SIZES':             ['Tiny', 'Small', 'Medium', 'Large', 'Huge'],
    'PLANET_GRAVITIES':         ['Low G', 'Normal G', 'Heavy G'],
    'PLANET_TERRAINS':          ['Toxic', 'Radiated', 'Baren', 'Desert', 'Tundra', 'Ocean', 'Swamp', 'Arid', 'Terran', 'Gaia', 'k', 'l'],
    'PLANET_MINERALS':          ['Ultra Poor', 'Poor', 'Abundant', 'Rich', 'Ultra Rich'],
    'PLANET_SPECIALS':          ['-', 'Wormhole', 'Space Debris', 'Pirate Cache', 'Gold Deposits', 'Gem Deposits', 'Natives', 'Splinter', 'Hero', 'Monster', 'Artifacts', 'Orion'],

    'PLAYER_COLORS':		["red", "yellow", "green", "white", "blue", "brown", "purple", "orange"],
    'PLAYER_PERSONALITIES':	["Xenophobic", "Ruthless", "Aggressive", "Erratic", "Honorable", "Pacifist", "Dishonored"],
    'PLAYER_OBJECTIVES':	["Diplomat", "Militarist", "Expansionist", "Technologist", "Industrialist", "Ecologist"],
    'PLAYER_GOVERMENTS':	["Feudal", "Confederation", "Dictatorship", "Imperium", "Democracy", "Federation", "Unification", "Galactic Unification"],

    'SHIP_SIZES':               ["Frigate", "Destroyer", "Cruiser", "Battleship", "Titan", "Doomstar"],
    'DRIVES':                   ["-", "Nuclear", "Fusion", "Ion", "Antimatter", "Hyperdrive", "Interphased", "no unit"],
    'ARMORS':                   ["-", "Titanium", "Tritanium", "Zortrium", "Neutronium", "Adamantium", "Xentronium"],
    'SHIELDS':                  ["-", "class 1", "class 3", "class 5", "class 7", "class 10"],
    'COMPUTERS':                ["-", "Electronic", "Optronic", "Positronic", "Cybertronic", "Moleculartronic"],
    'WEAPONS':                  ["None", "Mass Driver", "Gauss Cannon", "Laser Cannon", "Particle Beam", "Fusion Beam", "Ion Pulse Cannon", "Graviton Beam", "Neutron Blaster", "Phasor", "Disrupter", "Death Ray", "Plasma Cannon", "Spatial Compressor", "Nuclear Missile", "Merculite Missile", "Pulson Missile", "Zeon Missile", "Anti-Matter Torpedo", "Proton Torpedo", "Plasma Torpedo", "Nuclear Bomb", "Fusion Bomb", "Anti-Matter Bomb", "Neutronium Bomb", "Death Spore", "Bio Terminator", "Mauler Device", "Assault Shuttle", "Heavy Fighter", "Bomber", "Interceptor", "Stasis Field", "Anti-Missile Rocket", "Gyro Destabilizer", "Plasma Web", "Pulsar", "Black Hole Generator", "Stellar Converter", "Tractor Beam", "Dragon Breath", "Phasor Eye", "Crystal Ray", "Plasma Breath", "Plasma Flux", "Caustic Slime"],
    'WEAPON_ARCS':              ["-", "Forward", "Forward ext.", "", "Back ext.", "", "", "", "Back", "", "", "", "", "", "", "360", "x"],
    'WEAPON_MODS_BEAM':         ["-", "Heavy Mount", "Point Defense", "Armor piercing", "Continous", "No Range Dissipation", "Shield Piercing", "AutoFire"],
    'WEAPON_MODS_MISILLE':      ["-", "Enveloping", "Mirv", "ECCM", "Heavily Armored", "Fast", "Emimisions Guidance", "Overloaded"],

    'SHIP_EXP_LEVEL':           ["Green", "Regular", "Veteran", "Elite", "Ultra Elite"],

    'SHIP_SPECIALS':            [
			            ["unknown special 1", "Achilles Targeting Unit", "Augmented Engines", "Automated Repair Unit", "Battle Pods", "Battle Scanner", "Cloaking Device", "Damper Field"],
			            ["Displacement Device", "ECM Jammer", "Energy Absorber", "Extended Fuel Tanks", "Fast Missile Racks", "Hard Shields", "Heavy Armor", "High Energy Focus"],
			            ["Hyper X Capacitors", "Inertial Nullifier", "Inertial Stabilizer", "Lightning Field", "Multi-Phased Shields", "Multi-Wave ECM Jammer", "Phase Shifter", "Phasing Cloak"],
			            ["Quantum Dentonator", "Range Master Unit", "Reflection Field", "Reinforced Hull", "Scout Lab", "Security Stations", "Shield Capacitor", "Stealth Field"],
			            ["Structual Analyzer", "Sub Space Teleporter", "Time Warp Facilitator", "Transporters", "Troop Pods", "Warp Dissipator", "Wide Area Jammer", "unknown special 2"]
                                ],


    'STAR_SIZES':               ['Small', 'Medium', 'Large'],
    'STAR_CLASSES':             ['Blue', 'White', 'Yellow', 'Orange', 'Red', 'Gray', 'Black Hole'],

    'TECH_LIST':                ["Achilles Targeting Unit", "Adamantium Armor", "Advanced City Planning", "Advanced Damage Control", "Alien Management Center", "Android Farmers", "Android Scientists", "Android Workers", "Anti-Gravity Harness", "Anti-Matter Bomb", "Anti-Matter Drive", "Anti-Matter Torpedoes", "Anti-Missile Rockets", "Armor Barracks", "Artemis System Net", "Artifical Planet", "Assault Shuttles", "Astro University", "Atmospheric Renewer", "Augmented Engines", "Autolab", "Automated Factories", "Automated Repair Unit", "Battleoids", "Battle Pods", "Battle Scanner", "Battlestation", "Bio-Terminator", "Biomorphic Fungi", "Black Hole Generator", "Bomber Bays", "Capitol", "Class I Shield", "Class III Shield", "Class V Shield", "Class VII Shield", "Class X Shield", "Cloaking Device", "Cloning Center", "Colony Base", "Colony Ship", "Confederation", "Cyber-Security Link", "Cybertronic Computer", "Damper Field", "Dauntless Guidance System", "Death Ray", "Death Spores", "Deep Core Mining", "Core Waste Dumps", "Deuterium Fuel Cells", "Dimensional Portal", "Displacement Device", "Disrupter Cannon", "Doom Star Construction", "Reinforced Hull", "ECM Jammer", "Electronic Computer", "Emissions Guidance System", "Energy Absorber", "Biospheres", "Evolutionary Mutation", "Extended Fuel Tanks", "Fast Missile Racks", "Federation", "Fighter Bays", "Fighter Garrison", "Food Replicators", "Freighters", "Fusion Beam", "Fusion Bomb", "Fusion Drive", "Fusion Rifle", "Gaia Transformation", "Galactic Currency Exchange", "Galactic Cybernet", "Galactic Unification", "Gauss Auto-Cannon", "Graviton Beam", "Gyro Destabilizer", "Hard Shields", "Heavy Armor", "Heavy Fighter Bays", "Heightened Intelligence", "High Energy Focus", "Holo Simulator", "Hydroponic Farms", "Hyper Drive", "MegaFluxers", "Hyper-X Capacitors", "Hyperspace Communications", "Imperium", "Inertial Nullifier", "Inertial Stabilizer", "Interphased Drive", "Ion Drive", "Ion Pulse Cannon", "Iridium Fuel Cells", "Jump Gate", "Laser Cannon", "Laser Rifle", "Lightning Field", "Marine Barracks", "Mass Driver", "Mauler Device", "Merculite Missile", "Microbiotics", "Microlite Construction", "Outpost Ship", "Moleculartronic Computer", "Multi-Wave Ecm Jammer", "Multi-Phased Shields", "Nano Disassemblers", "Neural Scanner", "Neutron Blaster", "Neutron Scanner", "Neutronium Armor", "Neutronium Bomb", "Nuclear Bomb", "Nuclear Drive", "Nuclear Missile", "Optronic Computer", "Particle Beam", "Personal Shield", "Phase Shifter", "Phasing Cloak", "Phasor", "Phasor Rifle", "Planetary Barrier Shield", "Planetary Flux Shield", "Planetary Gravity Generator", "Planetary Missile Base", "Ground Batteries", "Planetary Radiation Shield", "Planetary Stock Exchange", "Planetary Supercomputer", "Plasma Cannon", "Plasma Rifle", "Plasma Torpedoes", "Plasma Web", "Pleasure Dome", "Pollution Processor", "Positronic Computer", "Powered Armor", "Pulse Rifle", "Proton Torpedoes", "Psionics", "Pulsar", "Pulson Missile", "Quantum Detonator", "Rangemaster Unit", "Recyclotron", "Reflection Field", "Robotic Factory", "Research Laboratory", "Robo-Miners", "Space Scanner", "Scout Lab", "Security Stations", "Sensors", "Shield Capacitors", "Soil Enrichment", "Space Academy", "Spaceport", "Spatial Compressor", "Spy Network", "Standard Fuel Cells", "Star Base", "Star Fortress", "Star Gate", "Stasis Field", "Stealth Field", "Stealth Suit", "Stellar Converter", "Structural Analyzer", "Sub-Space Communications", "Sub-Space Teleporter", "Subterranean Farms", "Survival Pods", "Tachyon Communications", "Tachyon Scanner", "Telepathic Training", "Terraforming", "Thorium Fuel Cells", "Time Warp Facilitator", "Titan Construction", "Titanium Armor", "Tractor Beam", "Transport", "Transporters", "Tritanium Armor", "Troop Pods", "Universal Antidote", "Uridium Fuel Cells", "Virtual Reality Network", "Warp Dissipater", "Warp Interdictor", "Weather Control System", "Wide Area Jammer", "Xeno Psychology", "Xentronium Armor", "Zeon Missile", "Zortrium Armor"]
}

def int2bin(n):
    if n < 0:
	return ""
    b = str(n % 2)
    while n > 0:
	n = n >> 1
	b = str(n % 2) + b
    return int(b)
# end func int2bin

def get_int(b0, b1, b2 = 0, b3 = 0):
    return b0 + (b1 << 8) + (b2 << 16) + (b3 << 24)
# end func get_int

def int2greek(i):
#    print i
    return ["I", "II", "III", "IV", "V"][i]
# end func int2greek

def show_txt(prefix, txt):
    for line in txt:
	if line == "-":
	    print prefix
	    print "%s----------" % prefix
	    print prefix
	else:
	    print "%s%s" % (prefix, line)
# end func show_txt


def show_colonies(colonies, planets, players):
    global DICTIONARY
    print "=== Colonies ==="
    print
    i = -1
    for colony in colonies:
	i += 1
	planet = planets[colony['planet_id']]
        print "COLONY ... #%.3i" % i
	print "	planet: %i (%i. orbit)" % (colony['planet_id'], planet['position'])
	print "		type: %s" % DICTIONARY['PLANET_TYPES'][planet['type']]
	print "		size: %s" % DICTIONARY['PLANET_SIZES'][planet['size']]
	print "		terrain: %s" % DICTIONARY['PLANET_TERRAINS'][planet['terrain']]
	print "		gravity: %s" % DICTIONARY['PLANET_GRAVITIES'][planet['gravity']]
	print "		minerals: %s" % DICTIONARY['PLANET_MINERALS'][planet['minerals']]

	print

	for k in ('colony', 'flags', 'foodbase', 'group', 'max_farms', 'max_population', 'parent_star', 'picture', 'special', 'terraformations'):
	    print "		%s ... %i" % (k, planets[colony['planet_id']][k])

	print

	print "	owner: %i (%s / %s)" % (colony['owner'], players[colony['owner']]['race'], players[colony['owner']]['emperor'])
	print "	is_outpost: %i" % colony['is_outpost']
	print "	population: %i" % colony['population']
	print "	marines: %i" % colony['marines']
	print "	armors: %i" % colony['armors']
#	for colonist in colony['colonists']:
#	    print "COLONY ... colonist: %i : %i : %i : %i" % (colonist['a'], colonist['b'], colonist['c'], colonist['d'])
#	for building in colony['buildings']:
#	    pass
#	    print "COLONY ... building: %i:" % building
	print
#	print colony
	keys = colony.keys()
	keys.sort()
	for k in keys:
	    print "	%s ... %s" % (k, colony[k])
	print "/"
	print
    return
# end func show_colonies

def show_players(players):
    global DICTIONARY
    print "=== Players ==="
    print 
    i = -1
    for player in players:
	i += 1
        print "PLAYER ... #%i ...race: %s" % (i, player['race'])
	if player.has_key('personality'):
	    print "PLAYER ... emperor: %s" % player['emperor']
	    print "PLAYER ... personality: %s" % DICTIONARY['PLAYER_PERSONALITIES'][player['personality']]
	    if player['objective'] == 100:
		    print "PLAYER ... objective: Human Player"
	    else:
#		    print "PLAYER ... objective: %i" % player['objective']
		    print "PLAYER ... objective: %s" % DICTIONARY['PLAYER_OBJECTIVES'][player['objective']]
	    print "PLAYER ... picture: %i" % player['picture']
	    print "PLAYER ... color: %i" % player['color']
	    print "PLAYER ... technologies: %s" % str(player['technologies'])
	    print "PLAYER ... prototypes: %s" % str(player['prototypes'])
	    print "PLAYER ... tributes: %s" % str(player['tributes'])
	if player.has_key('racepicks'):
	    print
	    keys = player['racepicks'].keys()
	    keys.sort()
	    for k in keys:
	        print "	%i ... %s" % (player['racepicks'][k], k)
	print "///"
    return
# end func show_players

def show_stars(stars):
    print "=== Stars ==="
    print
    for i in range(len(stars)):
	star = stars[i]
	txt = []
	txt.append("star_id: %i" % i)
	txt.append("name: %s" % star['name'])
	txt.append("position: %i, %i" % (star['x'], star['y']))
	txt.append("size: %s (%i)" % (DICTIONARY['STAR_SIZES'][star['size']], star['size']))
	txt.append("class: %s (%i)" % (DICTIONARY['STAR_CLASSES'][star['class']], star['class']))
	txt.append("special: %s (%i)" % (DICTIONARY['SYSTEM_SPECIALS'][star['special']], star['special']))
	txt.append("wormhole: %i" % star['wormhole'])
	txt.append("indictor: %i" % star['indictor'])
	txt.append("artemis: %i" % star['artemis'])
	txt.append("-")
	keys = star.keys()
	keys.sort()
	for k in keys:
	    txt.append("%s ... %s" % (k, star[k]))
	show_txt("STAR ... #%.2i ... " % i, txt)
#end func show_stars

def show_planets(planets, stars, colonies, players):
#    print "=== Planetary objects ==="
#    print
    i = -1
#    for i in range(len(planets)):
    for planet in planets:
	i += 1
#	planet = planets[i]
	txt = []
	if planet['type'] != 0:
	    txt.append("planet_id: %i" % i)
	    txt.append("star_id: %i" % i)
    	    txt.append("name: %s %s" % (stars[planet['parent_star']]['name'], int2greek(planet['position'])))
	    txt.append("type: %s (%i)" % (DICTIONARY['PLANET_TYPES'][planet['type']], planet['type']))
	    txt.append("size: %s (%i)" % (DICTIONARY['PLANET_SIZES'][planet['size']], planet['size']))
	    txt.append("gravity: %s (%i)" % (DICTIONARY['PLANET_GRAVITIES'][planet['gravity']], planet['gravity']))
	    txt.append("terrain: %s (%i)" % (DICTIONARY['PLANET_TERRAINS'][planet['terrain']], planet['terrain']))
	    txt.append("minerals: %s (%i)" % (DICTIONARY['PLANET_MINERALS'][planet['minerals']], planet['minerals']))
	    txt.append("food base: %i" % planet['foodbase'])
	    txt.append("number of terraformations: %i" % planet['terraformations'])
	    txt.append("planet special: %s (%i)" % (DICTIONARY['PLANET_SPECIALS'][planet['special']], planet['special']))
	    txt.append("flags: %.2x" % planet['flags'])
	    txt.append("colony_id: %i" % planet['colony'])
	    show_txt("PLANET ... #%.3i ... " % i, txt)
# end func show_planets

def show_heroes(heroes):
    i = -1
    for hero in heroes:
	i += 1
	print "hero #%i" % i
        print "    name: %s" % hero['name']
        print "    title: %s" % hero['title']
        print "    type: %i" % hero['type']
        print "    experience: %i" % hero['experience']
        print "    common_skills: %s" % str(hero['common_skills'])
        print "    special_skills: %s" % str(hero['special_skills'])
	if hero['type'] == 0:
	    if (hero['specialSkills'][0] &   1): print "        Engineer"
	    if (hero['specialSkills'][0] &   2): print "        Engineer*"
	    if (hero['specialSkills'][0] &   4): print "        Fighter Pilot"
	    if (hero['specialSkills'][0] &   8): print "        Fighter Pilot*"
	    if (hero['specialSkills'][0] &  16): print "        Galactic Lore"
	    if (hero['specialSkills'][0] &  32): print "        Galactic Lore*"
	    if (hero['specialSkills'][0] &  64): print "        Helmsman"
	    if (hero['specialSkills'][0] & 128): print "        Helmsman*"

	    if (hero['specialSkills'][1] &   1): print "        Navigator"
	    if (hero['specialSkills'][1] &   2): print "        Navigator*"
	    if (hero['specialSkills'][1] &   4): print "        Ordnance"
	    if (hero['specialSkills'][1] &   8): print "        Ordnance*"
	    if (hero['specialSkills'][1] &  16): print "        Security"
	    if (hero['specialSkills'][1] &  32): print "        Security*"
	    if (hero['specialSkills'][1] &  64): print "        Weaponry"
	    if (hero['specialSkills'][1] & 128): print "        Weaponry*"
        print "    tech1: %i" % hero['tech1']
        print "    tech2: %i" % hero['tech2']
        print "    tech3: %i" % hero['tech3']
        print "    picture: %i" % hero['picture']
	print
# end func show_heroes

def show_ships(ships, players, heroes, systems):
    global DICTIONARY
    i = -1
    for ship in ships:
	i += 1
        print "ship #" + str(i) + " @ 0x" + ("%X" % ship['offset'])
        print "    Name: %s" % ship['name']
        print "    Size: %s" % DICTIONARY['SHIP_SIZES'][ship['size']]
        print "    Shield: %s" % DICTIONARY['SHIELDS'][ship['shield']]
        print "    Drive: %s" % DICTIONARY['DRIVES'][ship['drive']]
        print "    Computer: %s" % DICTIONARY['COMPUTERS'][ship['computer']]
        print "    Armor: %s" % DICTIONARY['ARMORS'][ship['armor']]
        print "    Icon: %i" % ship['icon']
        print "    Build cost: %i" % ship['build_cost']
        print "    Beam Defense: %i" % ship['beam_defense']
        print "    Builder: %s (%s)" % (players[ship['builder']]['emperor'], players[ship['builder']]['race'])
        print "    Owner: %s" % players[ship['owner']]['race']
        print "    coordinates: %i, %i" % (ship['x'], ship['y'])
	if ship['system'] == 0xff:
            print "    In / To: Antares !" 
	else:
            print "    In / To: %s (#%i)" % (systems[ship['system']]['name'], ship['system'])
        print "    exp. level: %s" % DICTIONARY['SHIP_EXP_LEVEL'][ship['exp_level']]
        print "    exp. points: %i" % ship['exp_points']
        print "    Speed: %i" % ship['speed']
        print "    Turns left: %i" % ship['turns_left']
#	print "    term: %x" % ship['term']
        if ship['hero'] == 0xff:
            print "    hero: - (%i + %i)" % (ship['hero'], ship['herox'])
        else:
            print "    hero: %s (%i) + %i" % (heroes[ship['hero']]['name'], ship['hero'], ship['herox'])
	for special in ship['specials']:
	    a = special >> 8
	    b = special % 256
	    print "        special: %s" % DICTIONARY['SHIP_SPECIALS'][a][b]
	for weapon in ship['weapons']:
	    if weapon['weapon'] != 0xff:
#		print "        weapon: %ix %i" % (weapon['quantity'], weapon['weapon'])
		print "        weapon: %ix %s" % (weapon['quantity'], DICTIONARY['WEAPONS'][weapon['weapon']])
	print
# end func show_ships

def show_tree(players, stars, planets, colonies):
    global DICTIONARY

    print "number of stars:               %i" % len(stars)
    print "number of planetary objects:   %i" % len(planets)
    print "number of colonies:            %i" % len(colonies)
    print

    i, ii, iii = -1, -1, -1
    for star in stars:
	i += 1
	print "System #%i" % i
	print "    name: %s" % star['name']
	print "    coordinates: %i, %i" % (star['x'], star['y'])
	print "    class: %s" % DICTIONARY['STAR_CLASSES'][star['class']]
	print "    size: %s" % DICTIONARY['STAR_SIZES'][star['size']]
	print "    special: %s" % star['special']
	if star['wormhole'] != 0xff:
	    print "    wormhole to: %s (#%i)" % (stars[star['wormhole']]['name'], star['wormhole'])
	print "    indictor: %s" % star['indictor']
	print "    artemis: %s" % star['artemis']
	print "    objects: %s" % str(star['objects'])
	for object in star['objects']:
    	    print "        object: #%i" % object
	    if object == 0xffff:
		pass
	    else:
		planet = planets[object]
#    		print "        object: #%i" % object
		print "        name: %s %s" % (star['name'], int2greek(planet['position']))
    		print "        size: %s (%i)" % (DICTIONARY['PLANET_SIZES'][planet['size']], planet['size'])
    		print "        type: %s (%i)" % (DICTIONARY['PLANET_TYPES'][planet['type']], planet['type'])
		print "        gravity: %s" % DICTIONARY['PLANET_GRAVITIES'][planet['gravity']]
		print "        x07: 0x%.2x" % planet['x07']
		print "        terrain: %s" % DICTIONARY['PLANET_TERRAINS'][planet['terrain']]
		print "        minerals: %s" % DICTIONARY['PLANET_MINERALS'][planet['minerals']]
		print "        foodbase: %s" % planet['foodbase']
		print "        terraformations: %s" % planet['terraformations']
		print "        x0d: 0x%.2x" % planet['x0d']
		print "        x0e: 0x%.2x" % planet['x0e']
		print "        special: %s" % DICTIONARY['PLANET_SPECIALS'][planet['special']]
		print "        flags: 0x%.2x" % planet['flags']
		if (planet['colony'] != 0xffff) and (planet['colony'] != 65281):
		    print "            colony #%i" % planet['colony']
		    colony = colonies[planet['colony']]
		    print "            offset: 0x%.5x" % colony['offset']
		    print "            type: %s" % DICTIONARY['COLONY_TYPES'][colony['type']]
		    print "            owner: %s (%s, %i)" % (players[colony['owner']]['race'], players[colony['owner']]['emperor'], colony['owner'])
		    print "            marines: %i" % colony['marines']
		    print "            armors: %i" % colony['armors']
		    print "            population: %i" % colony['population']
#		    colonist_group = {
#			'farmer':		0,
#			'worker':		0,
#			'scientist':		0,
#			'android-farmer':	0,
#			'android-worker':	0,
#			'android-scientist':	0,
#			'native':		0,
#			'unknown':		0
#		    }
		    for colonist in colony['colonists']:
			print "                colonist /hex dump/ : %.2x %.2x %.2x %.2x /bin dump/ %.8i %.8i %.8i %.8i" % (colonist['a'], colonist['b'], colonist['c'], colonist['d'], int2bin(colonist['a']), int2bin(colonist['b']), int2bin(colonist['c']), int2bin(colonist['d']))
#        		colonistRace = colonist['a'] & 15
#        		colonistRace = (colonist['a'] >> 4)
                        colonistRace = (colonist['a'] & 112) >> 4
                        print "                    colonist race: %i (%.2x)" % (colonistRace, colonistRace)
#                        print "                colonist race: %.8i" % int2bin((colonist['a'] & 15))
                        print
                    print colony['buildings']
                print
#	print "    links: %s" % str((star['link1'], star['link2'], star['link3'], star['link4'], star['link5']))
        print
# end func show_tree



def show_save_game(filename):
    """
    
    """
    pass
    print filename

    filesize = os.path.getsize(filename)
    savefile = open(filename, 'rb')
    data = savefile.read(filesize)
    savefile.close()

    # 0x0025d ~ (n * 361)       ... colonies
    # 0x19a9b ~ 0x1aa0c         ... heroes
    # 0x1aa0f ~ 0x21f57         ... players
    # 0x21f58 ~ 0x22ff9         ... ships

#    HEROES	= savegame.read_heroes(data)
    PLAYERS	= savegame.read_players(data)
#    STARS	= savegame.read_stars(data)
#    PLANETS	= savegame.read_planets(data, STARS)
#    COLONIES	= savegame.read_colonies(data, PLANETS)
#    SHIPS	= savegame.read_ships(data)

#    return

#    show_heroes(HEROES)
    show_players(PLAYERS)
#    show_stars(STARS)
#    show_planets(PLANETS, STARS, COLONIES, PLAYERS)
#    show_colonies(COLONIES, PLANETS, PLAYERS)
#    show_tree(PLAYERS, STARS, PLANETS, COLONIES)
#    show_ships(SHIPS, PLAYERS, HEROES, STARS)
    return
    

    #   display Nebulae info
    print
    print "Nebulae info..."
    for i in range(4):
        offset = 0x31def + (5 * i)
        x = get_int(ord(data[offset + 0x00]), ord(data[offset + 0x01]))
        y = get_int(ord(data[offset + 0x02]), ord(data[offset + 0x03]))
        type = ord(data[offset + 0x04])
        print "    #" + str(i)
        print "        x: %i" % x
        print "        y: %i" % y
        print "        type: %i" % type

show_SAVE_GAME('../moo2/SAVE3.GAM')
