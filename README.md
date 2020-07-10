# python-media-console
A python-based media console to view media files from either a remote server, local server, or local file system.

## Installing dependencies (Linux):
- Chromium browser: `sudo apt-get install chromium-browser`
- Chromium driver: `sudo apt-get install chromium-chromedriver`
These are required for automatically opening the browser in kiosk mode with selenium.

## Setting up the project (Linux):
- Clone the repository to whichever directory you like.
- Create a virtual environment by running `python3 -m venv env` in the terminal window in the project's directory.
  - If the python3-venv package is not installed, run the `apt-get install python3-venv` command first.  You may need to use sudo.
- Activate the virtual environment by running `source env/bin/activate` in the terminal.  You should see (env) at the beginning of the command line now.
- To install the project's dependencies, run `pip3 install -r requirements.txt` in the terminal.