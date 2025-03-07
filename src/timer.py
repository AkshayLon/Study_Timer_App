import streamlit as st
import time

class TimerInterface:

    def __init__(self, header_name):
        st.title(header_name)
        self.time_display_placeholder = st.empty()
        if 'timer_running' not in st.session_state:
            st.session_state.timer_running = False
        if 'time_elapsed' not in st.session_state:
            st.session_state.time_elapsed = 0

    def _nice_display_time(self, total_seconds):
        hours = int(total_seconds/3600)
        mins = int((total_seconds%3600)/60)
        secs = total_seconds%60
        return f"{hours:02}:{mins:02}:{secs:02}"

    def run_interface(self, work_time):
        
        if st.button("Start Timer"):
            st.session_state.time_elapsed = 0
            st.session_state.timer_running = True

        if st.button("Stop Focus Session"):
            st.session_state.timer_running = False

        time_display = st.empty()

        while st.session_state.timer_running:
            time_display.write(self._nice_display_time(abs(work_time-st.session_state.time_elapsed)))
            time.sleep(1)
            st.session_state.time_elapsed += 1
            st.rerun()
