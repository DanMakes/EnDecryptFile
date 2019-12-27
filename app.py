from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config('SQLAlchemy_DATABASE_URL") = '' # Need to put link ClearDB Database (or any other Database)
  db = SQLAlchemy(app)         
     
@app.route('/')

    def index():
        return 'hello world'

if __name__ == '__main__':
  app.run(debug=True)
  
