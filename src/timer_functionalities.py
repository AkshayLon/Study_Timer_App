import streamlit as st
import time

class TimerInterface:

    def __init__(self, header_name, work_time):
        st.title(header_name)
