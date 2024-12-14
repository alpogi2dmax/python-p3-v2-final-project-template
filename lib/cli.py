# lib/cli.py

from helpers import (
    exit_program,
    list_teams,
    select_team,
    create_team,
    team_details,
    update_team,
    list_players,
    delete_team,
    select_player,
    draft_player,
    player_details,
    update_player,
    trade_player,
    negotiate_salary,
    waive_player
)

def main():
    while True:
        menu()
        choice = input("Enter Option: ")
        if choice == "E" or choice == "e":
            exit_program()
        elif choice == "1":
            list_teams()
        elif choice == "2":
            selected_team = select_team()
            if selected_team:
                team(selected_team)
        elif choice == "3":
            create_team()
        else:
            print()
            print("Invalid choice")
            print()

def greetings():
    print()
    print("************************************************************************")
    print()
    print("Welcome to the NBA Commissioner Database")
    print("As NBA Commissioner, you are tasked to maintain the NBA Teams and Roster")
    print()
    print("************************************************************************")


def menu():
    print()
    print('Main Menu')
    print("************************************************************************")
    print("Please select an option:")
    print()
    print("1. List all teams")
    print('2. Select team')
    print("3. Create a team")
    print()
    print("Select E or e to exit the program")
    print()

def team(selected_team):
    while True:
        team_menu(selected_team)
        choice = input("Enter Option: ")
        if choice == "<":
            break
        elif choice == "1":
            team_details(selected_team)
        elif choice == "2":
            update_team(selected_team)
        elif choice == "3":
            delete_team(selected_team)
            break
        elif choice == "4":
            list_players(selected_team)
        elif choice == "5":
            selected_player = select_player(selected_team)
            if selected_player:
                player(selected_player)
        elif choice == "6":
            draft_player(selected_team)
        else:
            print()
            print("Invalid choice")
            print()

def team_menu(selected_team):
    print(f'{selected_team.name} Team Menu')
    print("************************************************************************")
    print('Please select an option')
    print()
    print('1: Team details')
    print('2: Update team')
    print('3: Delete team')
    print('4: List players')
    print('5: Select player')
    print('6: Draft player')
    print()
    print("Select < to go back to the Main Menu")
    print()

def player(selected_player):
    while True:
        player_menu(selected_player)
        choice = input("Enter Option: ")
        if choice == "<":
            break
        elif choice == "1":
            player_details(selected_player)
        elif choice == "2":
            update_player(selected_player)
        elif choice == "3":
            trade_player(selected_player)
            break
        elif choice == "4":
            negotiate_salary(selected_player)
        elif choice == "5":
            waive_player(selected_player)
            break
        else:
            print()
            print("Invalid choice")
            print()

def player_menu(selected_player):
    print(f'{selected_player.name} Player Menu')
    print("************************************************************************")
    print('Please select an option')
    print()
    print('1: Player details')
    print('2: Update player')
    print('3: Trade player')
    print('4: Negotiate salary')
    print('5: Waive player')
    print()
    print("Select < to go back to the Team Menu")
    print()

if __name__ == "__main__":
    greetings()
    main()