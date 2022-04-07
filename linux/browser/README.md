# Linux + browser slack client

## Dependencies
Only tested in X11 session
* [python-systemd](https://github.com/systemd/python-systemd)
* [xdotool](https://github.com/jordansissel/xdotool)
* [xprintidle](https://github.com/g0hl1n/xprintidle)

## Usage

1. Open slack in your browser, it would be convenient to pin it in a fixed location
2. Fill in the parameters in `main.py` as comments according to your environments
3. Refer `slack-active.service` to configure a systemd user service, make sure to adjust `ExecStart` and enable it
4. Start the service and let the computer idle for your configured time and see if your screen is automatically focused on the slack tab in browser, and check your status in the top right corner

Note: You can refer system journal to view script log