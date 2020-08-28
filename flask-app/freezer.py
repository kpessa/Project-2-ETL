from flask_frozen import Freezer
from app import app

app.config.from_pyfile('settings.py')
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()