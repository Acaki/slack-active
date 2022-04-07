import datetime
import subprocess
import time

from systemd import journal

# The browser name you used to open slack
browser_name = "firefox"
# The tab idx your slack is opened at
slack_tab_idx = 1
work_hour_start = 8
work_min_start = 0
work_hour_end = 22
work_min_end = 0
# How many seconds to consider being idle
idle_interval = 900
# How frequent to check for idle in seconds
check_interval = 60
last_active_time = datetime.datetime.now()


def is_working_time(current_time):
    return current_time.weekday() < 5 and datetime.time(
        work_hour_start, work_min_start, 0
    ) <= current_time.time() <= datetime.time(work_hour_end, work_min_end, 0)


while True:
    now = datetime.datetime.now()
    idle_time = int(subprocess.run("xprintidle", capture_output=True).stdout or 0) / 1000
    if (
        (now - last_active_time).total_seconds() > idle_interval
        and idle_time > idle_interval
        and is_working_time(now)
    ):
        journal.send("Idle detected, switching to slack browser tab...")
        subprocess.call(
            [
                "xdotool",
                "search",
                "--desktop",
                "0",
                "--class",
                browser_name,
                "windowactivate",
                "--sync",
                "key",
                f"alt+{slack_tab_idx}",
            ]
        )
        last_active_time = now
    time.sleep(check_interval)
