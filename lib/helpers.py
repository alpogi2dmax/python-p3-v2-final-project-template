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
    print()
    for i, team in enumerate(teams):
        print(f'{i+1}: {team.city} {team.name}')
    print()
    print("****************************************")

def select_team():
    teams = Team.get_all()
    list_teams()
    print()
    try:
        id_ = int(input("Enter the team's number: "))
        print()
        if 1 <= id_ <= len(teams):
            team = Team.find_by_id(id_)
            if team:
                print(f'You have the selected the {team.city} {team.name}')
                print()
                return team
            else:
                print("Team not found.")
        else:
            print("Invalid team number.")
    except ValueError:
        print("Please enter a valid number.")
    return None

def create_team():
    print()
    print("****************************************")
    print()
    print("Create a new team")
    print()
    name = input("Enter the team's name: ")
    city = input("Enter the team's city: ")
    print()
    print("****************************************")
    try:
        team = Team.create(name, city)
        print()
        print(f'{team.city} {team.name} has been added!')
        list_teams()
    except Exception as exc:
        print('Error creating team: ', exc)

def team_details(team):
    print("****************************************")
    print()
    print('Team Details')
    print()
    print(f'Team Name: {team.name}')
    print(f'Team City: {team.city}')
    print(f'Team Salary Cap: ${team.salary_cap:,d}')
    print(f'Team Remaining Salary Allocation: ${team.salary_cap:,d}')
    print()
    print("****************************************")


def update_team(team):
    if not team:
        print("No team selected for update.")
        return
    
    print()
    print(f'Updating {team.city} {team.name} details')
    print()
    new_name = input("Enter new name: ")
    new_city = input("Enter new city: ")

    # Update the team with new data if provided
    team.name = new_name or team.name
    team.city = new_city or team.city
    team.update()

    print()
    print("****************************************")
    print()
    print(f'Team updated to {team.city} {team.name}')
    print()
    print("****************************************")
    print()

def delete_team(team):
    team.delete()
    print()
    print(f'{team.city} {team.name} has been deleted')
    list_teams()

def list_players(team):
    players = Player.get_all()
    print()
    print("****************************************")
    print()
    print(f'{team.city} {team.name} Roster')
    print()
    roster = [player for player in players if player.team_id == team.id]
    if len(roster) == 0:
        print(f"There are no players in the {team.name}'s roster. Please add players.")
    else:
        for i, player in enumerate(roster):
            print(f'{i+1}: {player.name}')
    print()
    print("****************************************")
    print()

def select_player(team):
    players = Player.get_all()
    list_players(team)
    roster = [player for player in players if player.team_id == team.id]
    if len(roster) == 0:
        return
    try:
        id_ = int(input("Enter the player's number: "))
        print()
        if 1 <= id_ <= len(roster):
            return roster[id_ - 1]
        else:
            print("Player not found.")
    except ValueError:
        print("Please enter a valid number.")
    return None

def draft_player(team):
    print()
    print('Enter Player Details')
    print()
    name = input("Enter player's name: ")
    position = input("Enter player's position: ")
    salary = int(input("Enter player's salary: "))

    try:
        player = Player.create(name, position, salary, team.id)
        print()
        print(f'{player.name} is added to the {team.name} roster')
        list_players(team)
    except Exception as exc:
        print("Error drafting player: ", exc)

def player_details(player):
    print("****************************************")
    print()
    print('Player Details')
    print()
    print(f'Name: {player.name}')
    print(f'Position: {player.position}')
    print(f'Salary: ${player.salary:,d}')
    print()
    print("****************************************")