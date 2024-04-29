import os
import shutil
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import operator



def new_player(directory_path):
    gen_list = os.listdir(directory_path)
    games_list = list(filter(lambda file: file.endswith('.csv'), gen_list))
    new_player = len(games_list) == 0
    return new_player


def print_games(directory_path):
    gen_list = os.listdir(directory_path)
    games_list = list(filter(lambda file: file.endswith('.csv'), gen_list))
    new = new_player(directory_path)
    if (new):
        print("\nGame history is empty\n")
    else:
        print("\nGames: \n")
        print(games_list)
        print("\n")


def attempt_bar(directory_path):
    print("\nBar Chart: \n")
    store = ""
    quiz = ""
    date = ""
    time = ""
    stuff = []
    for i in os.listdir(directory_path):
        stuff.append(i)
        under_split = str(i)[:-4].split('_')
        quiz = under_split[0]
        date_time = under_split[1].split('-')
        date = f'{date_time[0]}/{date_time[1]}/{date_time[2]}'
        time = f'{date_time[3]}:{date_time[4]}:{date_time[5]}'
        print(f'{len(stuff)-1}: {quiz} {date} {time}')

    num = input("Choose an option: ")
    csv_directory = stuff[int(num)]
    game = pd.read_csv(os.path.join(directory_path, csv_directory))
    correct = game['Actual Answer'] == game['Player Answer']
    correct_count = correct.sum()
    incorrect_count = len(game) - correct_count

    plt.bar(['Correct', 'Incorrect'], [correct_count, incorrect_count])
    plt.xlabel('Answer')
    plt.ylabel('Count')
    plt.title('Correct vs. Incorrect Answers')
    plt.show()


def day_bar(directory_path):
    print("\nBar Chart: \n")
    store = ""
    quiz = ""
    date = ""
    time = ""
    stuff = []
    alt = []
    for i in os.listdir(directory_path):
        stuff.append(i)
        under_split = str(i)[:-4].split('_')
        quiz = under_split[0]
        date_time = under_split[1].split('-')
        date = f'{date_time[0]}/{date_time[1]}/{date_time[2]}'
        time = f'{date_time[3]}:{date_time[4]}:{date_time[5]}'
        print(f'{len(stuff)-1}: {quiz} {date} {time}')
        alt.append(f'{len(stuff) - 1}: {quiz} {date} {time}')

    day = input("Input a month and a day Ex: 4/27: ")

    total_correct = 0
    total_incorrect = 0
    for i in range(len(alt)):
        if day in alt[i]:
            csv_directory = stuff[i]
            game = pd.read_csv(os.path.join(directory_path, csv_directory))
            correct = game['Actual Answer'] == game['Player Answer']
            correct_count = correct.sum()
            incorrect_count = len(game) - correct_count
            total_correct += correct_count
            total_incorrect += incorrect_count

    plt.bar(['Correct', 'Incorrect'], [total_correct, total_incorrect])
    plt.xlabel('Answer')
    plt.ylabel('Count')
    plt.title('Correct vs. Incorrect Answers')
    plt.show()

def month_bar(directory_path):
    print("\nBar Chart: \n")
    store = ""
    quiz = ""
    date = ""
    time = ""
    stuff = []
    alt = []
    for i in os.listdir(directory_path):
        stuff.append(i)
        under_split = str(i)[:-4].split('_')
        quiz = under_split[0]
        date_time = under_split[1].split('-')
        date = f'{date_time[0]}/{date_time[1]}/{date_time[2]}'
        time = f'{date_time[3]}:{date_time[4]}:{date_time[5]}'
        print(f'{len(stuff)-1}: {quiz} {date} {time}')
        alt.append(f'{len(stuff) - 1}: {quiz} {date} {time}')

    year = input("Input a year: ")
    month = input("Input a month: ")

    yearmonth = year + '/' + month
    total_correct = 0
    total_incorrect = 0
    for i in range(len(alt)):
        if yearmonth in alt[i]:
            csv_directory = stuff[i]
            game = pd.read_csv(os.path.join(directory_path, csv_directory))
            correct = game['Actual Answer'] == game['Player Answer']
            correct_count = correct.sum()
            incorrect_count = len(game) - correct_count
            total_correct += correct_count
            total_incorrect += incorrect_count

    plt.bar(['Correct', 'Incorrect'], [total_correct, total_incorrect])
    plt.xlabel('Answer')
    plt.ylabel('Count')
    plt.title('Correct vs. Incorrect Answers')
    plt.show()


def year_bar(directory_path):
    print("\nBar Chart: \n")
    store = ""
    quiz = ""
    date = ""
    time = ""
    stuff = []
    alt = []
    years = set()
    for i in os.listdir(directory_path):
        stuff.append(i)
        under_split = str(i)[:-4].split('_')
        quiz = under_split[0]
        date_time = under_split[1].split('-')
        date = f'{date_time[0]}/{date_time[1]}/{date_time[2]}'
        years.add(date_time[0])
        time = f'{date_time[3]}:{date_time[4]}:{date_time[5]}'
        print(f'{len(stuff) - 1}: {quiz} {date} {time}')
        alt.append(f'{len(stuff) - 1}: {quiz} {date} {time}')

    track = []
    for year in years:
        year_dict = {'year': '', 'correct': 0, 'incorrect': 0}  # Create a new year_dict for each file
        for file in stuff:
            if year in file:
                year_dict['year'] = year  # Set the year for the year_dict
                game = pd.read_csv(os.path.join(directory_path, file))
                correct = game['Actual Answer'] == game['Player Answer']
                correct_count = correct.sum()
                incorrect_count = len(game) - correct_count
                year_dict['correct'] += correct_count
                year_dict['incorrect'] += incorrect_count
        track.append(year_dict)  # Append the year_dict to track after looping through all years
    track.sort(key=operator.itemgetter('year'))
    print(track)
    percentages = [(entry['correct'] / (entry['correct'] + entry['incorrect'])) * 100 for entry in track]
    years = [entry['year'] for entry in track]

    plt.figure(figsize=(10, 6))
    plt.hist(range(len(years)), weights=percentages, bins=len(years), edgecolor='black')
    plt.title('Distribution of Percentage of Correct Answers')
    plt.xlabel('Year')
    plt.ylabel('Distribution')
    plt.xticks(range(len(years)), years)  # Set years as x-axis ticks
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def year_line(directory_path):
    print("\nLine Graph: \n")
    store = ""
    quiz = ""
    date = ""
    time = ""
    stuff = []
    alt = []
    years = set()
    for i in os.listdir(directory_path):
        stuff.append(i)
        under_split = str(i)[:-4].split('_')
        quiz = under_split[0]
        date_time = under_split[1].split('-')
        date = f'{date_time[0]}/{date_time[1]}/{date_time[2]}'
        years.add(date_time[0])
        time = f'{date_time[3]}:{date_time[4]}:{date_time[5]}'
        print(f'{len(stuff) - 1}: {quiz} {date} {time}')
        alt.append(f'{len(stuff) - 1}: {quiz} {date} {time}')

    track = []
    for year in years:
        year_dict = {'year': '', 'correct': 0, 'incorrect': 0}  # Create a new year_dict for each file
        for file in stuff:
            if year in file:
                year_dict['year'] = year  # Set the year for the year_dict
                game = pd.read_csv(os.path.join(directory_path, file))
                correct = game['Actual Answer'] == game['Player Answer']
                correct_count = correct.sum()
                incorrect_count = len(game) - correct_count
                year_dict['correct'] += correct_count
                year_dict['incorrect'] += incorrect_count
        track.append(year_dict)  # Append the year_dict to track after looping through all years
        track.sort(key=operator.itemgetter('year'))

    print(track)
    percentages = [(entry['correct'] / (entry['correct'] + entry['incorrect'])) * 100 for entry in track]
    years = [entry['year'] for entry in track]

    plt.figure(figsize=(10, 6))
    plt.plot(years, percentages, marker='o', linestyle='-')
    plt.title('Percentage of Correct Answers Over Years')
    plt.xlabel('Year')
    plt.ylabel('Percentage of Correct Answers')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def bar_chart_menu(directory_path):
    option = 'O'
    while option != '6':
        print("\nBar Chart Menu")
        print("1. View Performance on a given attempt")
        print("2. View Monthly Performance from a given Year")
        print("3. View Yearly Performance")
        print("6. Exit back to main menu\n")
        option = input("Please select an option: ")
        if option == '1':
            attempt_bar(directory_path)
        elif option == '2':
            month_bar(directory_path)
        elif option == '3':
            year_bar(directory_path)
        elif option == '6':
            print("\nExiting back to data model menu")
        else:
            print("\nSorry, invalid input. Please try again.\n")


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


def view_results(directory_path, user_ids):
    print(f"Loading results for folder {user_ids}\n")
    option = 'O'
    path = os.path.join(directory_path, user_ids)
    while (option != '6'):
        print("\nData Model Menu")
        print("1. Bar Charts")
        print("2. Line Graph of Performance Overtime:")
        print("6. Exit back to main menu\n")
        option = input("Please select an option: ")
        if option == '1':
            bar_chart_menu(path)
        if option == '2':
            year_line(path)
        elif option == '6':
            print("\nExiting back to main menu")
        else:
            print("\nSorry, invalid input. Please try again.\n")


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
            view_results(directory_path, u_id)
        elif option == '6':
            print("\nExiting menu")
        else:
            print("\nSorry, invalid input. Please try again.\n")

dir_path = "../Project/"
if (os.path.exists(dir_path) == False):
    os.mkdir(dir_path)
menu(dir_path, user_ids)
