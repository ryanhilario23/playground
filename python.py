from flask import Flask, render_template
app = Flask(__name__)
    
@app.route('/')
def hello_world():
    return 'Type "/play" in the URL to start!'

@app.route('/play')
def play_game():
    return render_template("index.html",boxes = 3)
    
if __name__=="__main__":
    app.run(debug=True)