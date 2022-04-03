# Loading environment variable from .env file
from dotenv import load_dotenv
load_dotenv()

# Importing all the routes
from routes import files, users

# Importing flask app
from server import app

app.run()

