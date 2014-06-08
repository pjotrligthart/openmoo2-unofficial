#import os

import moo2
import star
import colony
import rules

def stardate(i):
    s = str(i)
    return s[:-1] + "." + s[-1]
# /stardate

class Game:

    def __init__(self, rules, game_file = None):
	self.set_recount_flag(False)
        self.set_rules(rules)
	if game_file:
	    self.load_moo2_savegame(game_file)
    # /__init__

    def set_recount_flag(self, value):
	self.__recount = value

    def set_rules(self, rules):
        self.__rules = rules
    # /set_rules

    def init_stars(self):
        self.__stars_by_coords = {}

        for star_id in self.__stars:
            star = self.__stars[star_id]
            k = "%i:%i" % (star.get_x(), star.get_y())
            self.__stars_by_coords[k] = star
            num = 0
            for object in star.get_objects():
#               print "object: %i" % object
                if object != 0xffff:
                    num += 1
                    self.__planets[object].set_position(num)
    # /init_stars
        
    def init_colonies(self):
        for colony_id in self.__colonies:
            colony	= self.__colonies[colony_id]
            planet_id	= colony.get_planet_id()
            if colony.get_owner() < 0xff:
                planet      = self.__planets[planet_id]
                colony.assign_planet(self.__planets[planet_id])
                colony.set_name("%s %i" % (self.__stars[planet.get_star()].get_name(), planet.get_position()))
    # /init_colonies

    def init_heroes(self):
        self.__players_heroes = {}
        for hero_id in self.__heroes:
            hero = self.__heroes[hero_id]
            if hero['player'] != 0xFF:
                if not self.__players_heroes.has_key(hero['player']):
                    self.__players_heroes[hero['player']] = {}
                self.__players_heroes[hero['player']][hero['id']] = hero

                

#        print self.__players_heroes
    # /init_heroes

    def load_moo2_savegame(self, filename):
        """
        Loads the original MOO2 savegame
        """

        savegame = moo2.Moo2Savegame(filename)

#        filesize = os.path.getsize(filename)
#        savefile = open(filename, 'rb')
#        data = savefile.read(filesize)
#        savefile.close()

        self.__game     = savegame.parse_game()
        self.__galaxy   = savegame.parse_galaxy()

        self.__heroes   = savegame.parse_heroes()          # 100%
        self.__players  = savegame.parse_players()
        self.__stars    = savegame.parse_stars()
        self.__planets	= savegame.parse_planets(self.__stars)		# 100%
        self.__colonies	= savegame.parse_colonies()
        self.__ships	= savegame.parse_ships()		# 100%

        self.init_stars()
        self.init_colonies()
        self.init_heroes()
	
	self.recount()
    # /load_moo2_savegame
 

    def get_colony_leader(self, colony_id):
#        print self.__colonies[colony_id].is_outpost()
        colony_owner = self.__colonies[colony_id].get_owner()
#        print
#        print("colony_id ... %i" % colony_id)
#        print("colony_data ... %s" % self.__colonies[colony_id])
#        print(self.__colonies[colony_id].planet())
#        print
        parent_star = self.__colonies[colony_id].planet().get_star()
 #       print "Game::get_colony_leader() ... colony_id = %i, owner = %i, parent_star = %i" % (colony_id, colony_owner, parent_star)
        for hero_id in self.list_player_colony_leaders(colony_owner):
            if self.__heroes[hero_id]['location'] == parent_star:
                return self.__heroes[hero_id]
        return None
    # /get_colony_leader

    def list_area_tech_ids(self, research_area):
        techs = []
        for tech_id in self.__rules['tech_table']:
            if self.__rules['tech_table'][tech_id]['area'] == research_area:
                techs.append(tech_id)
        return sorted(techs)
    # /list_techs_by_area


    def recount_heroes(self):
        for hero_id, hero in self.__heroes.iteritems():
            hero['level'] = 0
            for level in self.__rules['hero_levels']:
                if hero['experience'] >= level:
                    hero['level'] += 1
#            print self.__heroes[hero_id]

    def recount_colonies(self):
        for colony_id in self.__colonies:
            print("Game::recount_colonies() ... colony_id = %i" % colony_id)
            if self.__colonies[colony_id].exists():
#                print("Game::recount_colonies() ... self.__colonies[%i].owner() = %i" % (colony_id, self.__colonies[colony_id].owner()))
                colony_leader = self.get_colony_leader(colony_id)
#                print "Game::recount_colonies() ... colony_id %i, leader = %s" % (colony_id, str(colony_leader))
#                for hero_id in self.__heroes:
 #               print
                self.__colonies[colony_id].recount(self.__rules, colony_leader, self.__players)
    # /recount_colonies

    def list_player_colony_leaders(self, player_id):
        list = {}
        if not self.__players_heroes.has_key(player_id):
            return list
        for hero_id in self.__players_heroes[player_id]:
            hero = self.__heroes[hero_id]
#            print hero
            if hero['type'] == 1:
                list[hero_id] = hero
        return list
    # /list_player_colony_leaders

    def list_player_officers(self, player_id):
        list = {}
        if not self.__players_heroes.has_key(player_id):
            return list
        for hero_id in self.__players_heroes[player_id]:
            hero = self.__heroes[hero_id]
#            print hero
            if hero['type'] == 0:
                list[hero_id] = hero
        return list
    # /list_player_colony_leaders

    def update_research(self, player_id, research_item):
	print("Game::set_research() ... player_id = %i, research_item = %i" % (player_id, research_item))
	player = self.__players[player_id]
	player.set_research_item(research_item)
	player.set_research_area(self.__rules['tech_table'][research_item]['area'])
        player.set_research_costs(rules.research_costs(self.__rules['research_areas'], player.get_research_area(), player.get_research()))
        player.set_research_turns_left(rules.research_turns(player.get_research_costs(), player.get_research_progress(), player.get_research()))
	return True
    # /update_research

    def recount_players(self):
        for player_id in self.__players:
            self.__players[player_id].set_research(0)
            self.__players[player_id].set_food(0)


        for colony_id in self.__colonies:
            if self.__colonies[colony_id].exists():
                owner = self.__colonies[colony_id].get_owner()
                self.__players[owner].add_research(self.__colonies[colony_id].get_research())
                self.__players[owner].add_food(self.__colonies[colony_id].get_food() - self.__colonies[colony_id].total_population())

	# hardcoded 8 players
        for player_id in range(8):
            player = self.__players[player_id]

            if player.alive():
		self.update_research(player_id, player.get_research_item())
#                player.print_debug()

            # refresh player's research_areas:
            research_areas = {}
            for res_id in self.__rules['research']:
#                print "                         AREA: %s" % res_id
                area_id = self.__rules['research'][res_id]['start_area']
#                print "                         start_area = %i" % area_id
                while 1:
#                    print "      checking area_id = %i" % area_id

                    if not self.__rules['research_areas'][area_id]['next']:
                        break

                    area_techs = self.list_area_tech_ids(area_id)
#                    print "          area_techs = %s" % str(area_techs)
                    new_area_id = 0
                    for tech_id in area_techs:
                        if player.knows_technology(tech_id):
#                            print "known tech! ... %i .. moving to next area" % tech_id
                            new_area_id = self.__rules['research_areas'][area_id]['next']
                            break
                            
                    if new_area_id:
                        area_id = new_area_id
#                        player['research_levels'][res_id] = area_id
                    else:
                        break

                research_areas[res_id] = self.list_area_tech_ids(area_id)
            player.update_research_areas(research_areas)
#            print "                    research_areas = %s" % str(player['research_areas'])

#            for tech_id in player['known_techs']:
#                tech = self.__rules['tech_table'][tech_id]
#                print "                         known = %s (area: %i)" % (tech['name'], tech['area'])
            # / refresh player's research_areas
    # /recount_players

    def recount(self):
        print "=== Recount Heroes ==="
        self.recount_heroes()

        print "=== Recount Colonies ==="
        self.recount_colonies()

        print "=== Recount Players ==="
        self.recount_players()
    # /recount


    def raise_population(self):
        for colony_id in self.__colonies:
            self.__colonies[colony_id].raise_population()
    # /raise_population

    def get_stars_for_player(self, player_id):
        stars = {}
        for star_id in self.__stars:
#            print("star_id = %i" % star_id)
#            print(" visited = %i" % star['visited'])
            st = self.__stars[star_id]
            if st.visited_by_player(player_id):
                stars[star_id] = st
            else:
                # FIXME: this part returns dict instead of object!
                stars[star_id] = star.UnexploredStar(star_id, st.get_x(), st.get_y(), st.get_size(), st.get_pict_type(), st.get_class())
        return stars
    # /get_stars_for_player

    def get_colonies_for_player(self, player_id):
        colonies = {}
        for colony_id in self.__colonies:
            col = self.__colonies[colony_id]
            if col.get_owner() == player_id:
                colonies[colony_id] = col
            else:
                colonies[colony_id] = colony.EnemyColony(colony_id, col.get_owner())
        return colonies

    def get_data_for_player(self, player_id):
        """
        this method returns data for one particular player and leave data for other players
        security reasons to prevent hacked clients to display data that player should not know
        """

#        player_number = player_id + 1

        colony_leaders = self.list_player_colony_leaders(player_id)
#        print "=== Colony Leaders: ==="
#        print colony_leaders
#        print "=== /Colony Leaders: ==="

        officers = self.list_player_officers(player_id)
#        print "=== Officers: ==="
#        print officers
#        print "=== Officers: ==="


        return {
            'rules':            self.__rules,
            'me':               self.__players[player_id],

            'galaxy':           self.__galaxy,
            'players':          self.__players,                             # insecure
            'stars':            self.get_stars_for_player(player_id),       # 100% secure?
            'stars_by_coords':  self.__stars_by_coords,                     # insecure

            'colony_leaders':   colony_leaders,                             # 50% secure?
            'officers':         officers,                                   # 50% secure?

            'planets':          self.__planets,                             # insecure
            'colonies':         self.get_colonies_for_player(player_id),      # 100% secured ?
            'ships':            self.__ships,                               # insecure
            'prototypes':       self.__players[player_id].get_prototypes(),    # 100% secured?
        }
    # /get_data_for_player

    def next_turn(self):
#        raise research_progress
#        raise population

        print
        print "##"
        print "#    NEW TURN!"
        print "##"
        print

        self.recount()

        for player_id in self.__players:
            player = self.__players[player_id]
            if player.alive():

                # research:
                if player.get_research_costs() > 0:
                    player.raise_research()
                    if player.reseatch_completed():
                        print "research completed"
                        print player.get_known_techs()
                        print player.get_research_item()
                        player.add_known_technology(player.get_research_item())
#
                        research_area_id = player.get_research_area()
#
                        if research_area_id:
                            research_area = self.__rules['research_areas'][research_area_id]
                            if research_area['next']:
                                player.set_research_area(research_area['next'])

                        player.set_research_progress(-1)
                # /research

                # BC:
                self.__players[player_id].raise_bc()
                # /BC

        self.raise_population()

        self.recount()

        self.__galaxy['stardate'] += 1
    # /next_turn

    def count_players(self):
	c = 0
	for player_id in range(8):
	    if self.__players[player_id].alive():
		c += 1
	return c
    # /count_players

    def show_stars(self):
	s = ['small', 'medium', 'large']
	c = ['blue', 'white', 'yellow', 'orange', 'red', 'gray', 'black hole']
	print
	print("+---------+-----------------+------------+------------+--------+-------+-------+-------+-------+-------+")
	print("| star_id | name            | coords     | class      | size   | obj 1 | obj 2 | obj 3 | obj 4 | obj 5 |")
	print("+---------+-----------------+------------+------------+--------+-------+-------+-------+-------+-------+")
	for star_id, star in self.__stars.items():
	    objects = star.get_objects()
	    print("| %7i | %15s | %4i, %4i | %10s | %6s | %5i | %5i | %5i | %5i | %5i |" % (star_id, star.get_name(), star.get_x(), star.get_y(), c[star.get_class()], s[star.get_size()], objects[0], objects[1], objects[2], objects[3], objects[4]))
	print("+---------+-----------------+------------+------------+--------+-------+-------+-------+-------+-------+")
    # /show_stars

    def show_planets(self):
	si = ['tiny', 'small', 'medium', 'large', 'huge']
	ty = ["???", "asteroid belt", "gas giant", "planet"]
	mi = ['ultra poor', 'poor', 'abundant', 'rich', 'ultra rich']
	te = ['toxic', 'radiated', 'baren', 'desert', 'tundra', 'ocean', 'swamp', 'arid', 'terran', 'gaia', '?? K ??', '?? L ??']
	print
	print("+-----------+-----------------+----------+--------+---------------+------------+----------+------+---------+")
	print("| planet_id | star            | position | size   | type          | minerals   | terrain  | food | max pop |")
	print("+-----------+-----------------+----------+--------+---------------+------------+----------+------+---------+")
	for planet_id, planet in self.__planets.items():
	    print("| %9i | %15s | %8i | %6s | %13s | %10s | %8s | %4i | %7i |" % (planet_id, self.__stars[planet.get_star()].get_name(), planet.get_position(), si[planet.get_size()], ty[planet.get_type()], mi[planet.get_minerals()], te[planet.get_terrain()], planet.get_foodbase(), planet.get_max_population()))
	print("+-----------+-----------------+----------+--------+---------------+------------+----------+------+---------+")
	print
    # /show_planets

    def show_players(self):
	print("NUMBER OF PLAYERS: %i" % self.count_players())
	print("+-----------+----------------------+----------------------+--------+--------+--------+----------------------+----------------------+---------+-----------+")
	print("| player_id | name                 | emperor              | food   | BC     | income | research:area        | :item                | :costs  | :progress |")
	print("+-----------+----------------------+----------------------+--------+--------+--------+----------------------+----------------------+---------+-----------+")
	for player_id, player in self.__players.items():
	    print("| %9i | %20s | %20s | %6i | %6i | %6i | %20s | %20s | %7i | %9i |" % (player_id, player.get_race_name(), player.get_emperor_name(), player.get_food(), player.get_bc(), player.get_bc_income(), str(player.get_research_area()), str(player.get_research_item()), player.get_research_costs(), player.get_research_progress()))
	print("+-----------+----------------------+----------------------+--------+--------+--------+----------------------+----------------------+---------+-----------+")
	print
    # /show_players

    def show_colonies(self):
	print
	print("+-----------+-----------+-----------------+------------+------+----------+----------+-------+")
	print("| colony_id | planet_id | owner           | population | food | research | industry | BC    |")
	print("+-----------+-----------+-----------------+------------+------+----------+----------+-------+")
	for colony_id, colony in self.__colonies.items():
	    planet_id = colony.get_planet_id()
	    owner_id = colony.get_owner()
	    if (planet_id < 0xFF) and (owner_id < 0xFF):
		owner = self.__players[owner_id]
		print("| %9i | %9i | %15s | %10s | %4i | %8i | %8i | %5i |" % (colony_id, planet_id, owner.get_race_name(), colony.get_population(), colony.get_food(), colony.get_research(), colony.get_industry(), colony.bc()))
	    else:
		print("| %9i | %9s | %15s | %10s | %4i | %8i | %8i | ----- |" % (colony_id, "0xFF", "0xFF", colony.get_population(), colony.get_food(), colony.get_research(), colony.get_industry()))
#	    colony = self.colonies
	print("+-----------+-----------+-----------------+------------+------+----------+----------+-------+")
	print
    # /show_colonies
	

    def show_ships(self):
	print
	print("+---------+-----------------+----------+------------+-----------------+-------+-------+")
	print("| ship_id | owner           | status   | coords     | destination     | speed | turns |")
	print("+---------+-----------------+----------+------------+-----------------+-------+-------+")
	for ship_id, ship in self.__ships.items():
	    if ship.exists():
		print("| %7i | %15s | %8s | %4i, %4i | %15s | %5i | %5i |" % (ship_id, self.__players[ship.get_owner()].get_race_name(), ship.get_status_text(), ship.get_x(), ship.get_y(), self.__stars[ship.get_destination()].get_name(), ship.get_travelling_speed(), ship.get_turns_left()))
	print("+---------+-----------------+----------+------------+-----------------+-------+-------+")
	print
