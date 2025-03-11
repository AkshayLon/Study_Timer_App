from datetime import datetime
import json, os, sqlite3

class SessionHandler:

    def __init__(self, distribution_data_file, history_data_file):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.distribution_data_file = os.path.join(script_dir, distribution_data_file)
        self._init_params_file()
        
        self.history_data_file = os.path.join(script_dir, history_data_file)
        self._init_history_file()
        
    def _init_params_file(self):
        if os.path.getsize(self.distribution_data_file)==0:
            init_data = {
                "distribution_params":None
            }
            with open(self.distribution_data_file, "w") as json_file:
                json.dump(init_data, json_file, indent=4)
    
    def _init_history_file(self):
        con = sqlite3.connect(self.history_data_file)
        cursor = con.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_time DATETIME,
                study_length INTEGER
            )
        """)
        con.commit()
        con.close()

    def export_focus_session(self, start_time, focus_time):
        con = sqlite3.connect(self.history_data_file)
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO history (start_time, study_length)
            VALUES (?, ?)
        """, (start_time, focus_time))
        con.commit()
        con.close()
