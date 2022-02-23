from flask import Flask, render_template, request
import math

app = Flask (__name__)

@app.route("/")
def about() :
    return render_template ('about.html')

@app.route("/about")
def about2() :
    return render_template ('about.html')


@app.route("/no1")
def No1() :
    return render_template ('No1.html')


@app.route('/no2',methods=['POST','GET'])
def No2():
    if request.method == 'POST':
        num = request.form ['number']
        result = math.sqrt(int(num))
        return render_template('No2_view.html', result=int(result))
    else:
        return render_template('No2.html')


@app.route("/no3", methods=['POST','GET']) 
def No3() :
    if request.method == 'POST':
        a = request.form ['sideA']
        b = request.form ['sideB']
        a = int(a)
        b = int(b)
        c = math.sqrt(int((a*a)+(b*b)))
        result = c
        return render_template('No3_view.html', result=int(result))
    else:
        return render_template ('No3.html')



if __name__ == '__main__':

    app.run(debug=True)