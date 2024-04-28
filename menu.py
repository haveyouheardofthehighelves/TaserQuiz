import os
import shutil
import subprocess
import pandas as pd

question_set1 = pd.read_csv("test.csv")
user_ids = pd.read_csv("user_ids.csv", dtype=str)


def delete_folders_files(directory_path):
    try:
        with os.scandir(directory_path) as folders:
            for folder in folders:
                if folder.is_file():
                    os.unlink(folder.path)
                else:
                    shutil.rmtree(folder.path)
            print("User folders deleted successfully\n")
    except OSError:
        print("Error deleteing folder\n")


def create_sub_folders(directory_path, user_ids):
    stop = False
    user_id = ""
    while (stop != True):
        print("\nHello new user!")
        user_id = str(input("Please enter your user id: "))
        there = False
        for i in range(user_ids.shape[0]):
            if user_id.strip() == str(user_ids.iloc[i]['User id']).strip():
                there = True
        if (there):
            directory = user_id
            path = os.path.join(directory_path, directory)
            if (os.path.exists(path) == False):
                os.mkdir(path)
                print(f"{user_id} Login successful\n")
                stop = True
            else:
                print(f"Already logged in\n")
                stop = True
        else:
            print("Invalid user id\n")
    return user_id


def show_list_dir(directory_path):
    dir_list = os.listdir(directory_path)
    if (len(dir_list) == 0):
        print("Project folder is empty\n")
    else:
        print("Project folder contents: ")
        print(dir_list)
        print("\n")


def play_game(user_ids):
    print(f"Loading game for folder {user_ids}\n")
    with open('current_player.txt', 'w+') as file:
        file.write(user_ids)
    subprocess.run(['python', 'FlashCards.py'], shell=True)


def view_results(user_ids):
    print(f"Loading results for folder {user_ids}\n")


def menu(directory_path, user_ids):
    option = 'O'
    u_id = create_sub_folders(directory_path, user_ids)
    while (option != '6'):
        print("1. Play game")
        print("2. View results")
        print("6. Exit\n")
        option = input("Please select an option: ")
        if option == '1':
            play_game(u_id)
        elif option == '2':
            view_results(u_id)
        elif option == '6':
            print("\nExiting menu")
        else:
            print("\nSorry, invalid input. Please try again.\n")


def get_accuracy(user_id, csv_file):
    pass


dir_path = "Project/"
if (os.path.exists(dir_path) == False):
    os.mkdir(dir_path)
else:
    menu(dir_path, user_ids)
