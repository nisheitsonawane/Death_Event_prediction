import pickle
from flask import Flask, render_template, request

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
@app.route('/predict',methods=['GET','POST'])
def predict():
    age=(request.form.get('age'))
    ef=(request.form.get('ejection_fraction'))
    sc=(request.form.get('serum_creatinine'))

    input_data=[[age,ef,sc]]

    prediction=model.predict(input_data)
    return render_template('index.html',pred_text=f"Person's survival Rate: {prediction} (0:Survived,1:not Survived)")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

