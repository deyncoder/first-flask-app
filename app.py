# Import flask
# import render_template to link the css file to html file
from flask import Flask, render_template

# Set app name to 'app'
app = Flask(__name__)
print(app)


# Use app decorator to create route. This route is the index root. This is so that when we launch application,
# we do not get 404, but the content we intended to. 

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) # Set this to 'false' when launching flask app to production env


