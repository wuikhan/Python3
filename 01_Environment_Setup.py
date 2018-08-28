# activate the environment
# 'conda env list' to check the list of all available environments
# 'source activate /anaconda3/envs/PFDS'
# 'conda list' to view all the installed packages


import webbrowser
import  time

total_break = 3
break_count = 0

print("This program started on " + time.ctime())

while(break_count < total_break):
    time.sleep(10)
    webbrowser.open("http://www.google.com")
    break_count = break_count + 1


