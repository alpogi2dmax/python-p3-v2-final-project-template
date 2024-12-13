# lib/cli.py

from helpers import (
    exit_program,
    list_teams,
    select_team,
    create_team,
    update_team,
    list_players,
    delete_team
)


def main():
    while True:
        menu()
        choice = input("Enter Option: ")
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

def greetings():
    print()
    print("****************************************")
    print()
    print("Welcome to the NBA Commissioner Database")
    print("As NBA Commissioner, you are tasked to maintain the NBA Teams and Roster")
    print()
    print("****************************************")


def menu():
    print()
    print("Please select an option:")
    print()
    print("0. Exit the program")
    print("1. List all teams")
    print('2. Select team')
    print("3. Create a team")
    print()

def team(selected_team):
    while True:
        team_menu()
        choice = input("Enter Option: ")
        if choice == "0":
            break
        elif choice == "1":
            update_team(selected_team)
        elif choice == "2":
            delete_team(selected_team)
            break
        elif choice == "3":
            list_players(selected_team)
        else:
            print("Invalid choice")

def team_menu():
    print('Please select an option')
    print()
    print('0: Go Back to main menu')
    print('1: Update team')
    print('2: Delete team')
    print('3: List players')
    print()

if __name__ == "__main__":
    greetings()
    main()