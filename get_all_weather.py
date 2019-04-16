from webapp import create_app
from webapp.wunderground_parser import get_python_weather

app = create_app()
with app.app_context():
    get_python_weather()
