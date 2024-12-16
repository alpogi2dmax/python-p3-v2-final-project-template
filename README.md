# NBA Commissioner's Database

## Introduction

Welcome to the NBA Commissioner's Database. This is a program utilizing CLI + ORM to help manage NBA teams and players. This will allow the user to navigate through each team, create new teams, add, delete, and transfer players between teams, and manage salary cap.

## Directory Structure

Please see directory structure below:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── player.py
    │   └── team.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py
```

Models would include player.py and team.py which would house the Player and Team class respectively. The Player class would include the Foreign Key. helpers.ph include all methods that are imported to cli.py for the Command Line Interface. I included seed.py for the initial data.

## How to Use

Please run the following commands before using:

```console
pipenv install
pipenv shell
python lib/seed.py
python lib/cli.py
```

## Features

### Main Menu

Once the program is launched, you have 3 options which are as follows:

    1. List all teams - It will list all existing teams in the database
    2. Select team - It will list all existing teams and allow you to select a team from the list
    3. Create a team - It will create a new team which will then be added to the list of teams.

Typing 'E' or 'e' will exit you from the program.

### Team Menu

If select team is selected among the options, it will enter a new loop which will be the Team Menu. It will list the team chosen and the following options:

    1. Team details
    2. Update team
    3. Delete Team
    4. List players
    5. Select player
    6. Draft player

Typing '<' will bring you back to the Main Menu.

The following options has these features:

* Team Details

This will list out the Team Name, City, Salary Cap and Remaining Salary allocations. Remaining salary allocation is the salary cap less the sum of all salaries in the roter. This is needed to determine if we can draft new players.

* Update Team

The Update Team option will let the user update the team name and city.

* Delete Team

The Delete Team option will let the user to delete the team from the database. However, if the team has players in its roster, it will prompt the user to either waive or draft all players before deleting the team.

* List Players

The List Players option will list all the players within the team. If there are no players in the team roster, it will prompt the user to add players.

* Select Player

The Select Player option will ask the user to select a player from the player list. If the team does not have anyone in the roster, the user will be prompted.

* Draft Player

The draft player option will allow the user to add a new player to the database and the team. If the team salary and new player's salary will exceed the salary cap, it will prompt the user the player cannot be drafted as it will exceed the salary limit.

### Player Menu

If Select Player is selected, the user will be brought to a new loop which will showcase the Player Menu. The Player Menu will show the Player name and the following options:

    1. Player details
    2. Update player
    3. Trade player
    4. Negotiate salary
    5. Waive player

Typing '<' will bring you back to the Team Menu.

The following options has these features:

* Player details

This will show the player's name, position, and salary.

* Update player

This will allow the user to update the player's name and position.

* Trade player

This will allow the user to transfer the player to another team. The player will then be removed from the current team roster then transferred to the other team's roster. This will also bring the user back to the Team Menu.

* Negotiate salary

This wil allow the user to change the player's salary. If the new salary and the team salary would exceed the team salary cap, the user will be prompted that the new salary is not allowed.

* Waive player

This will remove the player from the database as well as from the team. This will bring the user back to the team menu.

## Conclusion

This is a cool project that would allow the user to manage teams, players, and salaries.
