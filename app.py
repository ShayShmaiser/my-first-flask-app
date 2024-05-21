#same app with changes in order to test the "ansible"
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, welcome to my Flask app!'

# Define a route for a custom page
@app.route('/about')
def about():
    return 'This is a simple Flask app.'

# Define a route with a dynamic URL parameter
@app.route('/user/<username>')
def user_profile(username):
    return f'Welcome, {username}!'

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
