#coding=utf-8
from flask import *
from random import *
app = Flask(__name__)

# A function which judges win/lose/tie and return strings
def judge(choice, pc_choice): 
    if choice == pc_choice:
        return "It's Tie!"
    elif((choice=='r' and pc_choice=='s') or (choice=='s' and pc_choice=='p') or (choice=='p' and pc_choice=='s')):
        return "You Win!"
    else:
        return "You Lose!"
    
@app.route("/")  # Home page
def index():
    return render_template('lab10.html')

@app.route('/student_data', methods =['POST'])
def root():
    name = request.form['name'] # get name and student id strings
    id = request.form['id']
    print()
    print("name : "+ name)
    print("student_id : "+ id)
    print()
    return "ok"

@app.route('/rsp', methods = ['GET'])
def rsp():
    choice = request.args.get('choice') # Query String
    li=['r', 's', 'p']
    pc_choice = li[randint(0,2)]
    
    if choice not in li:
        return "Wrong input! Try again."
    else:
        print()
        print("computer: %s  user: %s" % (pc_choice, choice))
        print()
        return judge(choice, pc_choice)

app.run(host='192.168.137.97', port=3000, debug=True)