#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.team import Team
from models.player import Player

def seed_database():
    Player.drop_table()
    Team.drop_table()
    Team.create_table()
    Player.create_table()

    # Create seed data
    warriors = Team.create('Warriors', 'Golden State')
    lakers = Team.create('Lakers', 'Los Angeles')
    kings = Team.create('Kings', 'Sacramento')
    rockets = Team.create('Rockets', 'Houston')
    nets = Team.create('Nets', 'Brooklyn')
    Player.create('Steph Curry', 'Point Guard', 40000000, warriors.id)
    Player.create('Draymond Green', 'Power Forward', 20000000, warriors.id)
    Player.create('Andrew Wiggins', 'Small Forward', 15000000, warriors.id)


seed_database()
print("Seeded database")