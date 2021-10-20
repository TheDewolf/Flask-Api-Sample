from flask import Flask

# App name and configs
api = Flask(__name__)
api.config['JSON_SORT_KEYS'] = False

# Home route
@api.route("/")
def home():
    return {"status": "Server is up and running!"}

# Run the api
api.run()
