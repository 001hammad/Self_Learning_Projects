import streamlit as st
import datetime
import time
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Function to play alarm sound
def play_alarm():
    alarm_file = "alarm.mp3"
    if os.path.exists(alarm_file):
        pygame.mixer.music.load(alarm_file)
        pygame.mixer.music.play()
    else:
        st.error("❌ Alarm sound file not found!")

# Streamlit UI
st.title("⏰ Simple Alarm Clock")
st.write("Set an alarm and let it wake you up!")

# User input for alarm time
alarm_time = st.text_input("Enter Alarm Time (HH:MM:SS)", "07:30:00")

# Live clock update area
time_display = st.empty()

# Button to set alarm
if st.button("Set Alarm"):
    try:
        # Validate input format
        time.strptime(alarm_time, "%H:%M:%S")
        st.success(f"✅ Alarm set for {alarm_time}. Waiting...")

        # Loop to check time
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            time_display.write(f"⏳ Current Time: {current_time}")
            
            if current_time == alarm_time:
                st.warning("⏰ Time's up! Wake up! 🔔")
                play_alarm()
                break

            time.sleep(1)  # Wait 1 second before updating

    except ValueError:
        st.error("❌ Invalid format! Please enter time in HH:MM:SS format.")
