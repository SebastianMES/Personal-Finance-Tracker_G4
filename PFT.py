#Personal Finance Tracker App - Group 4
#Collaborators
# -Grace Jeong
# -Cristian Camilo Salamanca
# -Sebastian Melendez

# import the main libraries
from datetime import datetime
import pandas as pd

# global variables:
task_df = pd.DataFrame(columns=['Task','Priority', 'Deadline', 'Priority_Value','Complete'])
today_date = datetime.today().date()
changes_unsaved = False

def main():
    while True:
        print("Personal Finance Tracker Application")
        print()