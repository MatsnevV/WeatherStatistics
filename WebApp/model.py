from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class weather_data(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        #id_city = db.Column(db.Integer,nullable=False)
        data = db.Column(db.DateTime, unique=True, nullable=False)
        wind = db.Column(db.Integer, nullable=True)
        wet = db.Column(db.Integer, nullable=True)
        pressure = db.Column(db.Integer, nullable=True)
        temp = db.Column(db.Integer, nullable=True)
        wind_dark = db.Column(db.Integer, nullable=True)
        wet_dark = db.Column(db.Integer, nullable=True)
        pressure_dark = db.Column(db.Integer, nullable=True)
        temp_dark = db.Column(db.Integer, nullable=True)
        text = db.Column(db.Text, nullable=True)

        def __repr__(self):
            return f'<weather_data {self.data}>'


class weather_data_history(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        #id_city = db.Column(db.Integer,nullable=False)
        data = db.Column(db.DateTime, unique=True, nullable=False)
        wet = db.Column(db.Integer, nullable=True)
        pressure = db.Column(db.Integer, nullable=True)
        temp = db.Column(db.Integer, nullable=True)
        temp_max = db.Column(db.Integer, nullable=True)
        temp_min = db.Column(db.Integer, nullable=True)
        text = db.Column(db.Text, nullable=True)