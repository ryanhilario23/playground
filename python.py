from flask import Flask, render_template
app = Flask(__name__)
    
@app.route('/')
def hello_world():
    return 'Type "/play" in the URL to start!'

@app.route('/play')
def play_game():
    return render_template("index.html",nums = 3,color='lightblue')
    
@app.route('/play/<int:num>')
def level_two(num):
    return render_template("index.html",nums=num, color='lightblue')

@app.route('/play/<int:num>/<string:color>')
def level_three(num,color):
    return render_template("index.html",nums=num, color=color)


if __name__=="__main__":
    app.run(debug=True)