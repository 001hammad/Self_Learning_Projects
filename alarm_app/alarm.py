import streamlit as st
import datetime
import time
import os

# 🌟 Streamlit UI Config
st.set_page_config(page_title="Alarm Clock", page_icon="⏰", layout="centered")

# 🎨 Custom CSS for Stylish UI
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #141E30, #243B55);
            color: white;
            font-family: Arial, sans-serif;
        }
        .clock-container {
            background: rgba(0, 0, 0, 0.7);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.3);
        }
        h1 {
            font-size: 50px;
            font-weight: bold;
            text-shadow: 3px 3px 5px rgba(255, 255, 255, 0.3);
        }
        .live-clock {
            font-size: 28px;
            font-weight: bold;
            color: #ffcc00;
            text-shadow: 2px 2px 4px black;
        }
        .stButton>button {
            background: linear-gradient(to right, #ff8000, #ffcc00);
            color: black;
            font-weight: bold;
            padding: 12px 20px;
            font-size: 18px;
            border-radius: 10px;
            box-shadow: 0px 5px 10px rgba(255, 255, 255, 0.3);
            transition: 0.3s ease-in-out;
        }
        .stButton>button:hover {
            transform: scale(1.1);
            background: linear-gradient(to right, #ffcc00, #ff8000);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ UI Content Inside a Styled Box
st.markdown("<div class='clock-container'>", unsafe_allow_html=True)
st.markdown("<h1>⏰ Digital Alarm Clock</h1>", unsafe_allow_html=True)
st.markdown("<h3>Never miss an important moment!</h3>", unsafe_allow_html=True)

# 🕒 Live clock display
time_display = st.empty()

# 🔽 User input for alarm time
alarm_time = st.text_input("Enter Alarm Time (HH:MM:SS)", "07:30:00")

# ✅ Set Alarm button (Centered)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    set_alarm = st.button("🔔 Set Alarm", use_container_width=True)

if set_alarm:
    try:
        # ✅ Validate time format
        time.strptime(alarm_time, "%H:%M:%S")
        st.success(f"✅ Alarm set for {alarm_time}")

        # 🕒 Real-time clock update
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            time_display.markdown(f"<div class='live-clock'>⏳ Current Time: {current_time}</div>", unsafe_allow_html=True)
            
            if current_time == alarm_time:
                st.warning("⏰ Time's up! Wake up! 🔔")

                # ✅ **Auto-Play Sound in Streamlit**
                audio_file = "alarm.mp3"  # Ensure this file exists in your project
                if os.path.exists(audio_file):
                    st.audio(audio_file, format="audio/mp3", autoplay=True)
                else:
                    st.error("❌ Alarm sound file not found!")

                break

            time.sleep(1)  # Wait 1 second before updating

    except ValueError:
        st.error("❌ Invalid format! Please enter time in HH:MM:SS format.")

st.markdown("</div>", unsafe_allow_html=True)
