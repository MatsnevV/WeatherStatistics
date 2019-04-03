from flask_sqlalchemy import SQLAlchemy

class weather(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        url = db.Column(db.String, unique=True, nullable=False)
        published = db.Column(db.DateTime, nullable=False)
        text = db.Column(db.Text, nullable=True)
    
        id = db.Column(db.Integer, primary_key=True)
        data = db.Column(db.DateTime, nullable=False)
        wind = db.Column(db.integer, nullable=False)
        wet = db.Column(db.integer, nullable=False)
        pressure = db.Column(db.integer, nullable=False)
        temp = db.Column(db.Integer, nullable=False)
        wind_dark = db.Column(db.integer, nullable=False)
        wet_dark = db.Column(db.integer, nullable=False)
        pressure_dark = db.Column(db.integer, nullable=False)
        temp_dark = db.Column(db.integer, nullable=False)
        text = db.Column(db.Text, nullable=True)

        def __repr__(self):
            return '<News {self.title} {}>'.format(self.title, self.url)