import os
import datetime

def get_mood_input():
    valid_moods = {
        'happy': 2,
        'relaxed': 1,
        'apathetic': 0,
        'sad': -1,
        'angry': -2
    }
    
    while True:
        mood = input("Enter your current mood (happy, relaxed, apathetic, sad, angry): ").strip().lower()
        if mood in valid_moods:
            return valid_moods[mood]
        print("Invalid mood. Please try again.")

def has_entered_mood_today():
    today = str(datetime.date.today())
    with open("data/mood_diary.txt", "r") as file:
        return any(line.split()[1] == today for line in file)


def assess_mood():
    if has_entered_mood_today():
        print("Sorry, you have already entered your mood today.")
        return
    mood = get_mood_input()
    with open("data/mood_diary.txt", "a") as file:
        file.write(f"{mood} {datetime.date.today()}\n")
    
    data_dir = "data"
    file_path = os.path.join(data_dir, "mood_diary.txt")
    
    with open(file_path, "r") as file:
        lines = file.readlines()[-7:]
    
    if len(lines) < 7:
        print("Not enough data to assess mood disorders.")
        return
    
    mood_scores = [int(line.strip().split()[0]) for line in lines]
    average_mood = sum(mood_scores) // len(mood_scores) if mood_scores else 0
    mood_count = [0] * 5
    for score in mood_scores:
        mood_count[score+2] += 1
    
        
    if mood_count[4] >= 5:
        diagonosis = "manic"
    elif mood_count[1] >= 4:
        diagonosis = "depressive"
    elif mood_count[2] >= 6:
        diagonosis = "schizoid"
    else:
        diagonosis = {2: "happy", 1: "relaxed", 0: "apathetic", -1: "sad", -2: "angry"}[average_mood]
    
    print(f"Your diagnosis: {diagonosis}!")