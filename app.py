from flask import Flask, render_template
from os import walk
from threading import Timer
from selenium import webdriver
import subprocess
import json

app = Flask(__name__)

myAppsJSON = open('myapps.json')
myApps = json.load(myAppsJSON)
configJSON = open('config.json')
config = json.load(configJSON)

@app.route('/')
def index():
    return render_template('index.html', title='My Apps', myApps=myApps, numApps=len(myApps))

@app.route('/music')
def music():
    musicFileDirectory = config['mediaSources'][0]+'Music/'
    musicFiles = []
    for (dirpath, dirnames, filenames) in walk(musicFileDirectory):
        for filename in filenames:
            musicFiles.append("http://127.0.0.1:8000/Music/"+filename)
    return render_template('music.html', title="Music", musicFiles=musicFiles, numMusicFiles=len(musicFiles))

@app.route('/videos')
def videos():
    return "videos"

def doAppSetup():
    # Start the chromium web broswer
    chromeOptions = webdriver.ChromeOptions()
    if (not config["debug"]):
        chromeOptions.add_argument('--kiosk')
    chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chromeOptions)
    driver.get('http://127.0.0.1:5000')

    # Run a simple http server on a local directory
    serverCommand = "cd " + config['mediaSources'][0] + " ; python3 -m http.server"
    runServerCommand = subprocess.Popen(serverCommand, stdout=subprocess.PIPE, shell=True)
    runServerCommand.communicate()

if __name__ == '__main__':
    Timer(1, doAppSetup).start()
    app.run()
