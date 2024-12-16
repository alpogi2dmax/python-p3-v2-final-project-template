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

Models would include player.py and team.py which would house the Player and Team class respectively. The Player class would include the Foreign Key. helpers.ph include all methods that are imported to cli.py for the Command Line Interface.

