from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/studytimer')
def studytimer():
    return render_template('studytimer.html')

@app.route('/todolist')
def todolist():
    return render_template('todolist.html')

@app.route('/songlist')
def songlist():
    return render_template('songlist.html')
@app.route('/easteregg')
def easteregg():
    return render_template('easteregg.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
