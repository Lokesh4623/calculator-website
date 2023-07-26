from flask import Flask,request,jsonify,render_template
app=Flask(__name__)
from command_line_calculator_v2 import calculate,prec
@app.route('/')
def home():
  return render_template('calculator_v1.html')
@app.route('/predict1',methods=['POST']) 
def predict():
  exp=request.form['exp'] 
  result=calculate(exp)
  return render_template('calculator_v1.html',result_text=str(result))
if __name__=="__main__":
  app.run(debug=True)