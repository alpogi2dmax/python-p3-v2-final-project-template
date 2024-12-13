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
    warriors = Team.create('Warriors', 'Golden State', 150000000)
    lakers = Team.create('Lakers', 'Los Angeles', 150000000)
    kings = Team.create('Kings', 'Sacramento', 150000000)
    rockets = Team.create('Rockets', 'Houston', 150000000)
    nets = Team.create('Nets', 'Brooklyn', 150000000)
    Player.create('Steph Curry', 'Point Guard', 40000000)
    Player.create('Draymond Green', 'Power Forward', 20000000)
    Player.create('Andrew Wiggins', 'Small Forward', 15000000)


seed_database()
print("Seeded database")