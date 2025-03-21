import pandas as pd
import numpy as np
import random

# User-defined Inputs
num_subjects = 6  # Number of subjects (excluding labs)
num_labs = 2  # Number of lab sessions
total_courses = num_subjects + num_labs

# Let users define subjects dynamically
subjects = {}
for i in range(1, num_subjects + 1):
    subjects[f"Subject {i}"] = f"Professor {i}"
for i in range(1, num_labs + 1):
    subjects[f"Lab {i}"] = f"Lab Instructor {i} (Lab)"

# Timetable settings
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_slots = ["9AM-10AM", "10AM-11AM", "11AM-12PM", "1PM-2PM", "2PM-3PM", "3PM-4PM"]
labs = [f"Lab {i}" for i in range(1, num_labs + 1)]  # Labs require 2-hour slots

# Create an empty timetable
timetable = pd.DataFrame(index=days, columns=time_slots)

# Assign Subjects & Labs
assigned_slots = []
for day in days:
    available_subjects = list(subjects.keys())
    
    for slot in time_slots:
        if available_subjects:
            subject = random.choice(available_subjects)
            professor = subjects[subject]

            # Ensure no professor is double-booked
            if any(professor in row for row in timetable.values):
                continue  # Skip if already booked

            # Assign labs in 2-hour slots
            if subject in labs and time_slots.index(slot) < len(time_slots) - 1:
                timetable.loc[day, slot] = f"{subject} ({professor})"
                timetable.loc[day, time_slots[time_slots.index(slot) + 1]] = f"{subject} (Contd.)"
                available_subjects.remove(subject)
            else:
                timetable.loc[day, slot] = f"{subject} ({professor})"
                available_subjects.remove(subject)

# Fill empty slots with "Free Period"
timetable.fillna("Free Period", inplace=True)

# Display the timetable
print(timetable)

# Save to CSV for easy access
timetable.to_csv("generated_timetable.csv")


