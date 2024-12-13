from models.team import Team
from models.player import Player

def exit_program():
    print("Goodbye!")
    exit()

def list_teams():
    teams = Team.get_all()
    print()
    print("****************************************")
    print()
    print('NBA Teams')
    for i, team in enumerate(teams):
        print(f'{i+1}: {team.city} {team.name}')
    print()
    print("****************************************")
    print()

def select_team():
    teams = Team.get_all()
    list_teams()

    try:
        id_ = int(input("Enter the team's number: "))
        if 1 <= id_ <= len(teams):
            team = Team.find_by_id(id_)
            if team:
                print(f'Selected Team: {team.city} {team.name}')
                return team
            else:
                print("Team not found.")
        else:
            print("Invalid team number.")
    except ValueError:
        print("Please enter a valid number.")
    return None

def create_team():
    name = input("Enter the team's name: ")
    city = input("Enter the team's city: ")
    salary_cap = int(input("Enter the team's salary cap: "))

    try:
        team = Team.create(name, city, salary_cap)
        print(f'{team.city} {team.name} have been added!')
        list_teams()
    except Exception as exc:
        print('Error creating team: ', exc)

def update_team(team):
    if not team:
        print("No team selected for update.")
        return
    
    print(f'Updating {team.city} {team.name}')
    new_name = input("Enter new name: ")
    new_city = input("Enter new city: ")
    new_salary_cap = int(input("Enter new salary cap: "))

    # Update the team with new data if provided
    team.name = new_name
    team.city = new_city
    team.salary_cap = new_salary_cap
    team.update()

    print(f'Team updated to {team.city} {team.name}')

def list_players(team):
    players = Player.get_all()
    print()
    print("****************************************")
    print()
    print(f'{team.city} {team.name} Roster')
    print()
    for i, player in enumerate(players):
        if player.team_id == team.id:
            print(f'{i+1}: {player.name}')
    print()
    print("****************************************")
    print()
