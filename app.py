from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config('SQLAlchemy_DATABASE_URL") = '' # Need to put link ClearDB Database (or any other Database)
  db = SQLAlchemy(app)         
     
           Class User(db.Model):
                 id = db.Column(db.Integer, primary_key=True)
                 username = db.Column(db.String(100), nullable=False, unique=True)
                 email = db.Column(db.String(120), nullable=False, unique=True)
                 password = db.Column(db.String(120), nullable=False)
                 date_created = db.Column(db.DateTime, default=datetime.utcnow) 

@app.route('/')
    def index():
        return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
 
