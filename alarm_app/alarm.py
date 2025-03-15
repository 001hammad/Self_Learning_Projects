import streamlit as st
import datetime
import time
import pygame
import os

# 🎵 Initialize pygame mixer
pygame.mixer.init()

# ✅ Function to play alarm sound
def play_alarm():
    alarm_file = "alarm.mp3"

    if not os.path.exists(alarm_file):
        st.error("❌ Alarm sound file not found!")
        return

    try:
        pygame.mixer.music.load(alarm_file)
        pygame.mixer.music.play()
    except Exception as e:
        st.error(f"⚠️ Sound error: {e}")

# 🌟 Streamlit UI (MODERN & CLEAN)
st.set_page_config(page_title="Alarm Clock", page_icon="⏰")

# 🏆 Stylish heading
st.markdown(
    "<h1 style='text-align: center; font-size: 36px;'>⏰ Digital Alarm Clock</h1>",
    unsafe_allow_html=True
)

st.write("Set an alarm and let it wake you up!")

# 🕒 Live clock display
time_display = st.empty()

# 🔽 User input for alarm time
alarm_time = st.text_input("Enter Alarm Time (HH:MM:SS)", "07:30:00")

# ✅ Set Alarm button
if st.button("🔔 Set Alarm"):
    try:
        # ✅ Validate time format
        time.strptime(alarm_time, "%H:%M:%S")
        st.success(f"✅ Alarm set for {alarm_time}")

        # 🕒 Real-time clock display after button click
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            time_display.markdown(f"<h2 style='text-align: center;'>⏳ Current Time: {current_time}</h2>", unsafe_allow_html=True)
            
            if current_time == alarm_time:
                st.warning("⏰ Time's up! Wake up! 🔔")
                play_alarm()  # 🎵 Play alarm sound
                break

            time.sleep(1)  # Wait 1 second before updating

    except ValueError:
        st.error("❌ Invalid format! Please enter time in HH:MM:SS format.")
