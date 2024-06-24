#coding=utf-8
from flask import *
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

dict={}
dict_json = json.dumps(dict, ensure_ascii=False)
# let ensure_ascii=False so that we can see Chinese....Maybe?

@app.route('/')
def index():
    return render_template('lab10_plus.html') # Home Page

@app.route('/set', methods = ['POST'])
def root():
    name = request.form['store_name'] # get store_name & score from the form
    score = request.form['score']
    dict[name]=score # create a dict
    dict_json = json.dumps(dict, ensure_ascii=False)
    # turn dict into json form so that we can see the dictionary in the website

    print()
    print('user input data : %s' % str(request.form.to_dict()) )
    print()
    print('Data on server : %s' % str(dict))
    print()
    return render_template('lab10_plus.html', dict_json=dict_json)
    # return 'lab10_plus.html' and 'dict_json' so that the variable dict_json can be used in html

@app.route('/reset/<op>', methods = ['GET'])
def reset(op):
    if op=='y': # clear elements in dict
        dict.clear()
        dict_json = json.dumps(dict, ensure_ascii=False)
        print()
        print('Data on server : %s' % str(dict))
        print()
        return render_template('reset.html')
    else:
        dict_json = json.dumps(dict, ensure_ascii=False) 
        return render_template('lab10_plus.html', dict_json=dict_json)
        # just show the original page if op!='y'

app.run(host='192.168.137.97', port=3000, debug=True)