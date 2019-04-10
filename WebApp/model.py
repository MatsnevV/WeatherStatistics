from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class weather(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        #id_city = db.Column(db.Integer,nullable=False)
        data = db.Column(db.DateTime, unique=True, nullable=False)
        wind = db.Column(db.Integer, nullable=False)
        wet = db.Column(db.Integer, nullable=False)
        pressure = db.Column(db.Integer, nullable=False)
        temp = db.Column(db.Integer, nullable=False)
        wind_dark = db.Column(db.Integer, nullable=False)
        wet_dark = db.Column(db.Integer, nullable=False)
        pressure_dark = db.Column(db.Integer, nullable=False)
        temp_dark = db.Column(db.Integer, nullable=False)
        text = db.Column(db.Text, nullable=True)

        def __repr__(self):
            return f'<weather {self.data}>'


