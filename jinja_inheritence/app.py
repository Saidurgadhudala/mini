from flask import Flask,render_template
app=Flask('__name__')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/input')
def input():
    return render_template('input.html')
app.run(debug=True)