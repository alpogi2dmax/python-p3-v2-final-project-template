from models.team import Team
from models.player import Player

def exit_program():
    print()
    print("************************************************************************")
    print()
    print('Thank your visiting. Goodbye!')
    print()
    print("************************************************************************")
    print()
    exit()

def list_teams():
    teams = Team.get_all()
    print()
    print("************************************************************************")
    print()
    print('NBA Teams')
    print()
    for i, team in enumerate(teams):
        print(f'{i+1}: {team.city} {team.name}')
    print()
    print("************************************************************************")
    return teams

def select_team():
    teams = list_teams()
    print()
    id = int(input("Enter the team's number: "))
    print()
    try:
        if 1 <= (id) <= len(teams):
            team = teams[(id) - 1]
            if team:
                print(f'You have the selected the {team.city} {team.name}')
                print()
                return team
            else:
                print("Team not found.")
        else:
            print("Invalid team number.")
    except Exception as exc:
        print('Error creating team: ', exc)
    return None

def create_team():
    print()
    print("************************************************************************")
    print()
    print("Create a new team")
    print()
    name = input("Enter the team's name: ")
    city = input("Enter the team's city: ")
    print()
    print("************************************************************************")
    try:
        team = Team.create(name, city)
        print()
        print(f'{team.city} {team.name} has been added!')
        list_teams()
    except Exception as exc:
        print('Error creating team: ', exc)

def team_details(team):
    players = team.players()
    team_salaries = sum([player.salary for player in players])
    print("************************************************************************")
    print()
    print('Team Details')
    print()
    print(f'Team Name: {team.name}')
    print(f'Team City: {team.city}')
    print(f'Team Salary Cap: ${team.salary_cap:,d}')
    print(f'Team Remaining Salary Allocation: ${(team.salary_cap - team_salaries):,d}')
    print()
    print("************************************************************************")


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
    print("************************************************************************")
    print()
    print(f'Team updated to {team.city} {team.name}')
    print()
    print("************************************************************************")
    print()

def delete_team(team):
    players = team.players()
    if len(players) > 0:
        print()
        print("************************************************************************")
        print()
        print('Roster must be empty. Please waive or trade players before deleting')
        print()
        print("************************************************************************")
    else:
        team.delete()
        print()
        print(f'{team.city} {team.name} has been deleted')
        list_teams()

def list_players(team):
    players = team.players()
    # players = Player.get_all()
    print()
    print("************************************************************************")
    print()
    print(f'{team.city} {team.name} Roster')
    print()
    # roster = [player for player in players if player.team_id == team.id]
    if len(players) == 0:
        print(f"There are no players in the {team.name}'s roster. Please add players.")
    else:
        for i, player in enumerate(players):
            print(f'{i+1}: {player.name}')
    print()
    print("************************************************************************")
    print()
    return players

def select_player(team):
    # change id_ to id
    players = list_players(team)
    if len(players) == 0:
        return
    try:
        id = int(input("Enter the player's number: "))
        print()
        if 1 <= id <= len(players):
            return players[id - 1]
        else:
            print("Player not found.")
    except ValueError:
        print("Please enter a valid number.")
    return None

def draft_player(team):
    players = team.players()
    team_salaries = sum([player.salary for player in players])
    print()
    print('Enter Player Details')
    print()
    name = input("Enter player's name: ")
    position = input("Enter player's position: ")
    salary = int(input("Enter player's salary: "))

    try:
        if team_salaries + salary > team.salary_cap:
            print()
            print('Salaries will exceed salary cap. Please review salary allocation.')
            print()
        else:
            player = Player.create(name, position, salary, team.id)
            print()
            print(f'{player.name} is added to the {team.name} roster')
            list_players(team)
    except Exception as exc:
        print("Error drafting player: ", exc)

def player_details(player):
    print("************************************************************************")
    print()
    print('Player Details')
    print()
    print(f'Name: {player.name}')
    print(f'Position: {player.position}')
    print(f'Salary: ${player.salary:,d}')
    print()
    print("************************************************************************")
    print()

def update_player(player):
    if not player:
        print("No player selected for update.")
        return
    
    print()
    print(f'Updating {player.name} details')
    print()
    player_details(player)

    new_name = input("Enter new name: ")
    new_position = input("Enter new position: ")

    # Update the player with new data if provided
    player.name = new_name or player.name
    player.position = new_position or player.position
    player.update()
    print()
    print("************************************************************************")
    print()
    print(f'Updated {player.name} details')
    print()
    print("************************************************************************")
    print()
    print('Player Details')
    print()
    print(f'Name: {player.name}')
    print(f'Position: {player.position}')
    print()
    print("************************************************************************")
    print()

def negotiate_salary(player):
    rosters = Player.get_all()
    team_salaries = sum([roster.salary for roster in rosters if roster.team_id == player.team_id])
    team_salary_cap = Team.get_all()[player.team_id -1].salary_cap
    if not player:
        print("No player selected for update.")
        return
    print()
    print(f"Negotiating {player.name}'s salary")
    print()
    print(f"Current Salary: ${player.salary:,d}")
    print(f"Remaining Salary Allocation: ${(team_salary_cap - team_salaries):,d}")
    print()

    new_salary = input("Enter proposed salary: ")

    # Update the player with new data if provided
    if team_salaries + int(new_salary) > Team.get_all()[player.team_id -1].salary_cap:
        print()
        print('Salaries will exceed salary cap. Please review salary allocation.')
        print()
    else:
        player.salary = int(new_salary) if new_salary != '' else player.salary
        player.update()
        print()
        print("************************************************************************")
        print()
        print(f"Negotiated {player.name}'s details")
        print()
        print("************************************************************************")
        print()
        print(f"{player.name}'s new salary: ${player.salary:,d}")
        print()
        print("************************************************************************")
        print()


def trade_player(player):
    if not player:
        print("No player selected for update.")
        return
    
    print()
    print(f'Trading {player.name}')
    print()
    list_teams()
    new_team_id = input('Enter new team number: ')

    # Update the player with new data if provided
    teams = Team.get_all()
    if int(new_team_id) > len(teams):
        print('Invalid Team number. Choose a valid number.')
        return
    elif 1 <= int(new_team_id) <= len(teams):
        player.team_id = int(new_team_id)
        player.update()
    print()
    print("************************************************************************")
    print()
    print(f'Traded {player.name} to the {teams[int(new_team_id)-1].name}')
    print()

def waive_player(player):
    team = Team.get_all()[player.team_id -1]
    player.delete()
    print()
    print(f'{player.name} has been waived')
    list_players(team)