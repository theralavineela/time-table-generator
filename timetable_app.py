import streamlit as st
import pandas as pd
import numpy as np
import random

# Title
st.title("📅 AI-Based Automated Timetable & Resource Scheduler")

# Sidebar inputs
st.sidebar.header("Enter Scheduling Details")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
num_periods = st.sidebar.number_input("Number of periods per day", min_value=1, max_value=10, value=5)
num_classrooms = st.sidebar.number_input("Number of classrooms", min_value=1, max_value=10, value=3)

# Faculty & Subjects Input
num_faculty = st.sidebar.number_input("Number of faculty", min_value=1, max_value=10, value=5)
faculty_list = [st.sidebar.text_input(f"Faculty {i+1} Name", value=f"Faculty {i+1}") for i in range(num_faculty)]

num_subjects = st.sidebar.number_input("Number of subjects", min_value=1, max_value=10, value=5)
subject_list = [st.sidebar.text_input(f"Subject {i+1}", value=f"Subject {i+1}") for i in range(num_subjects)]

# Generate Timetable Button
if st.sidebar.button("Generate Timetable"):
    timetable = []
    
    for day in days:
        for period in range(num_periods):
            classroom = f"Classroom {random.randint(1, num_classrooms)}"
            subject = random.choice(subject_list)
            faculty = random.choice(faculty_list)

            # Avoid double-booking the same faculty in the same period
            while any(row['Faculty'] == faculty and row['Day'] == day and row['Period'] == period + 1 for row in timetable):
                faculty = random.choice(faculty_list)
            
            timetable.append({"Day": day, "Period": period + 1, "Classroom": classroom, "Subject": subject, "Faculty": faculty})

    # Convert to DataFrame
    df = pd.DataFrame(timetable)

    # Display timetable
    st.subheader("📌 Generated Timetable")
    st.write(df)

    # Download option
    csv = df.to_csv(index=False)
    st.download_button("Download Timetable", data=csv, file_name="timetable.csv", mime="text/csv")
