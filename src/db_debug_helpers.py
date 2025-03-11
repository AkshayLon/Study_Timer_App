import os, sqlite3

def debug_print_db(cursor_object):
    cursor_object.execute("SELECT * FROM history")
    data_rows = cursor_object.fetchall()
    for row in data_rows:
        print(row)

def debug_wipe_db(cursor_object):
    cursor_object.execute("DELETE FROM history")

if __name__=="__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = "..\\data\\sessions.db"
    file_path = os.path.join(script_dir, db_path)
    
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    
    # CALL DEBUG FUNCTIONS HERE
    debug_wipe_db(cursor)
    debug_print_db(cursor)
    ###

    con.commit()
    con.close()

