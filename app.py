from flask import Flask, render_template
import json
app = Flask(__name__)

myAppsJSON = open('myapps.json')
myApps = json.load(myAppsJSON)

@app.route('/')
def index():
    return render_template('index.html', title='Home', myApps=myApps, numApps=len(myApps))

@app.route('/music')
def music():
    return render_template('music.html', title="Music")

@app.route('/videos')
def videos():
    return "videos"

if __name__ == '__main__':
    app.run()
