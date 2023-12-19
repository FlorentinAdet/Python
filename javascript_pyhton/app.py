# app.py
from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder="./")

@app.route("/") 
def hello(): 
    return render_template('index.html')

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route('/nb_maj')
def compter_majuscules():
    text = request.args.get('text', '')
    from example import compter_majuscules
    result = compter_majuscules(text)
    return result

@app.route('/call_python_function')
def call_python_function():
    # Get parameters from the query string
    param1 = request.args.get('name', default=None, type=str)
    param2 = request.args.get('age', default=None, type=int)
    
    from example import python_function
    result = python_function(param1, param2)
    response = make_response(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
      app.run(debug=True)