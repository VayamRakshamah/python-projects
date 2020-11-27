from flask import Flask, render_template

#variable to store flask instance
app = Flask(__name__)
#decorator
@app.route('/')
#this function defines what the webpage will do
def home():
    return render_template("home.html")

@app.route('/about/')
#this function defines what the webpage will do
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
    