# lib/models/team.py
from models.__init__ import CURSOR, CONN

class Team:

    all = {}

    def __init__(self, name, city, salary_cap = 200000000, id =None):
        self.id = id
        self.name = name
        self.city = city
        self.salary_cap = salary_cap
    
    def __repr__(self):
        return f"<Team {self.id}: {self.name}, {self.city}, {self.salary_cap}>"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError('Name must be a non-empty string.')
        
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city) > 0:
            self._city = city
        else:
            raise ValueError('City must be a non-empty string.')
        
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Team instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT,
            city TEXT,
            salary_cap INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Team instances"""
        sql = """
            DROP TABLE IF EXISTS teams;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name, city, and salary_cap values of the current Team instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO teams (name, city, salary_cap)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.city, self.salary_cap))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, city):
        """ Initialize a new Team instance and save the object to the database """
        team = cls(name, city)
        team.save()
        return team
    
    def update(self):
        """Update the table row corresponding to the current Team instance."""
        sql = """
            UPDATE teams
            SET name = ?, city = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.city, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Team instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM teams
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        #Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Team object having the attribute values from the table row."""

        #Check the dictionary for an existing instance using the row's primary key
        team = cls.all.get(row[0])
        if team:
            # ensure attribute match row values in case local instance was modified
            team.name = row[1]
            team.city = row[2]
            team.salary_cap = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            team = cls(row[1], row[2], row[3])
            team.id = row[0]
            cls.all[team.id] = team
        return team
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Team object per fow in the table"""
        sql = """
            SELECT *
            FROM teams
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Team object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM teams
            WHERE id = ?
        """
    
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Team object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM teams
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def players(self):
        pass