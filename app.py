import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False) 

@app.route('/')     
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c085d66223d57c9b3393eb8f4b03aad0'

    city ='iowa'

    r = requests.get(url.format(city)).json()
    weather ={
        'city': city,
        'temparature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }    
    print(weather)
    return render_template('index.html', weather=weather)


if __name__ == "__main__":
    app.run()