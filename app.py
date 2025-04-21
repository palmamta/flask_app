from flask import Flask,render_template,url_for,request,redirect,jsonify


app = Flask(__name__)


@app.route("/",methods=['GET'])
def index():
    return "Welcome Page"

@app.route('/<name>')
def welcome_name(name):
    return f"Hello {name}"

@app.route('/success/<int:score>')
def success(score):
    return "Person has passed and score is "+str(score)

@app.route('/fail/<score>')
def fail(score):
    return 'Person has failed and score is '+str(score)

@app.route("/avg_marks", methods=["GET","POST"])
def find_avg():
    if request.method == "GET":
        return render_template('form.html')
    else:
        sub1 = float(request.form['sub1'])
        sub2 = float(request.form['sub2'])
        sub3 = float(request.form['sub3'])
        sub4 = float(request.form['sub4'])
        sum = sub1+sub2+sub3+sub4
        avg = (sub1+sub2+sub3+sub4)/4
        res = ''
        if avg < 50:
            res = "fail"
        else:
            res = 'success'
        print(sub1,sub2,sub3,sub4)
        return redirect(url_for(res,score=avg))
@app.route('/api',methods=['POST'])
def api_endpoint():
    input_val = request.get_json()
    a_val = float(dict(input_val)['a'])
    b_val = float(dict(input_val)['b'])
    return jsonify(a_val+b_val)

if __name__=="__main__":
    app.run(debug=True)

