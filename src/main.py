from timer import TimerInterface
from session_manager import SessionHandler

if __name__=="__main__":
    data_object = SessionHandler("..\\data\\params.json", "..\\data\\sessions.db")
    current_timer = TimerInterface("Study Timer", data_object)
    current_timer.run_interface(work_time=10)
