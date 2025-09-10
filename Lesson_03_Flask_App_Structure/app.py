from flask import Flask
app = Flask(__name__)

@app.route('/') # / Front Door (home page)
def home(): #Function name (can be anything)
    return "Home Page!" #What Visitors see
    
@app.route('/about')
def about():
    return """<h1> Welcome!</h1>
    <p> This is my first website </p>"""

@app.route('/contact')
def about():
    return "Contact Page!"

app.run(debug=True)