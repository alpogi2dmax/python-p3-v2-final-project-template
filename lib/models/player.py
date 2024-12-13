# lib/models/player.py
from models.__init__ import CURSOR, CONN
from models.team import Team

class Player:

    #Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, position, salary, team_id, id=None):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.team_id = team_id

    def __repr__(self):
        return (
            f'<Player {self.id}: {self.name}, {self.position}, {self.salary}, ' +
            f'Team ID: {self.team_id}>'
        )
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError('Name must be a non-empty string')
        
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, position):
        if isinstance(position, str) and len(position) > 0:
            self._position = position
        else:
            raise ValueError('Position must be a non-empty string')
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int) and 500000 <= salary <=50000000:
            self._salary = salary
        else:
            raise ValueError('Salary must be an integer and betweekn 500k and 50 million.')
        
    @property
    def team_id(self):
        return self._team_id
    
    @team_id.setter
    def team_id(self, team_id):
        if type(team_id) is int and Team.find_by_id(team_id):
            self._team_id = team_id
        else:
            raise ValueError('team_id must reference a team in the database.')
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Player instances """
        sql = """
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            position TEXT,
            salary INTEGER,
            team_id INTEGER,
            FOREIGN KEY (team_id) REFERENCES team(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Player instances """
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """Insert a new row with the name, position, salary, and team id values of the current Player object.
        Update object id attribute using the primary key of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO players (name, position, salary, team_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.position, self.salary, self.team_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        """Update the table row corresopnding to the current Player instance."""
        sql = """
            UPDATE players
            SET name = ?, position = ?, salary = ?, team_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.position, self.salary, self.team_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Player instance,
        delete the dictionary entry, reassign the attribute"""

        sql = """
            DELETE FROM players
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, position, salary, team_id):
        """ Initialize a new Player instance and save the object to the database """
        player = cls(name, position, salary, team_id)
        player.save()
        return player
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a player object having the attribute values from the table row."""

        #Check the dictionary for existing instance using the row's primary key
        player  = cls.all.get(row[0])
        if player:
            #ensure attributes match row values in case local instance was modified
            player.name = row[1]
            player.position = row[2]
            player.salary = row[3]
            player.team_id = row[4]
        else:
            #not in dictionary, crate new instance and add to dictionary
            player = cls(row[1], row[2], row[3], row[4])
            player.id = row[0]
            cls.all[player.id] = player
        return player
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Player object per table row"""
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Player object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM players
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return Player object corresponding to first table row matching the specified name"""
        sql = """
            SELECT *
            FROM players
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
