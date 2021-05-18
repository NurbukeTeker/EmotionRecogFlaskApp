from flask import Flask, render_template, Response, request, json, redirect, url_for ,send_from_directory

from datetime import datetime
from flask_apscheduler import APScheduler
import os
import sqlite3 as sql
# import notify2
import random
import jaydebeapi
import sys
from werkzeug.utils import secure_filename

#!/usr/bin/env python3
#!/usr/bin/env python2
# argv = sys.argv

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
IMAGE_SIZE = (224, 224)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from user import User
global User
tempUser = User("")


def get_user_data():
  if tempUser.userisIn() :
      return True
  tempUser.update()
  return False



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS 


@app.route('/')
def index(imagesource_='file://null'): 
  print(imagesource_,"in index")
  username = os.environ['USER'].title()
  if get_user_data():
    title = 'SisaFormatC-Home'
    return render_template('home.html', imagesource=imagesource_)
  else:
    title = 'SisaFormatC'
    return render_template('index.html')

@app.route('/userDetailStore', methods=['POST'])
def userDetailStore():
  email =  request.form['email'];
  time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
  return redirect("/")

@app.route('/emotion_count', methods=['POST'])
def getEmotionCount():
  user = os.environ['USER'].title()
  date = datetime.now().strftime("%d-%m-%Y")
 
  print("{'Neutral':2, 'Happy':2, 'Sad':2, 'Angry':2, 'Fear':7, 'Surprise':3}")
  return json.dumps({'Neutral':30, 'Happy':30, 'Sad':30, 'Angry':10, 'Fear':5, 'Surprise':5})


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print("HERREEE")
    if request.method == 'POST':
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
    print(file_path)
    return render_template("home.html", imagesource=file_path)



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == "__main__":
   scheduler = APScheduler()
   # scheduler.add_job(func=show_joke, args=['Joke Start'], trigger='interval', id='job', seconds=600)
   scheduler.start()
   app.run(host = '127.0.0.1', port= '5000',debug=True, threaded=False)