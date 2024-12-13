# lib/cli.py

from helpers import (
    exit_program,
    list_teams,
    select_team,
    create_team,
    update_team,
    list_players
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
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
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all teams")
    print('2. Select team')
    print("3. Create a team")

def team(selected_team):
    while True:
        team_menu()
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            update_team(selected_team)
        elif choice == "2":
            list_players(selected_team)
        else:
            print("Invalid choice")

def team_menu():
    print('Please select an option')
    print('0: Go Back to main menu')
    print('1: Update team')
    print('2: List players')

if __name__ == "__main__":
    main()