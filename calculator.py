from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

@app.route('/calculator',methods=['GET','POST'])
def cal():
    if request.method=='POST':
        a=request.json['num1']
        b=request.json['num2']
    operation = request.json['operation']
    if operation == 'Add':
        result = a + b
        res = 'the sum of ' + str(a)+ '&' + str(b)+ 'is'+str(result)
    elif operation == 'Sub':
        result = a - b
        res = 'the difference of ' + str(a)+ '&' + str(b)+ 'is' + str(result)
    elif operation == 'Div':
        result = a / b
        res = 'the Division of ' + str(a)+ '&' +str(b)+ 'is' + str(result)
    elif operation == 'Mul':
        result = a * b
        res = 'the Division of '+ str(a)+ '&' +str(b)+ 'is' +str(result)

    return jsonify(res)

if __name__=='__main__':
    app.run(port=800)

