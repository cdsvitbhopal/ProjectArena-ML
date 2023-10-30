from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
lr = pickle.load(open('Breast.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
  
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        radius_mean = float(request.form['rmean'])
        texture_mean = float(request.form['tmean'])
        smoothness_mean = float(request.form['smmean'])
        compactness_mean = float(request.form['cmean'])
        symmetry_mean = float(request.form['symean'])
        fractal_dimension_mean = float(request.form['fdmean'])
        texture_se = float(request.form['tse'])
        smoothness_se = float(request.form['smse'])
        symmetry_se = float(request.form['syse'])
        symmetry_worst = float(request.form['sywt'])

        values = np.array([[radius_mean,texture_mean, smoothness_mean, compactness_mean, symmetry_mean, fractal_dimension_mean,
                            texture_se, smoothness_se, symmetry_se, symmetry_worst]])
        prediction = lr.predict(values)
      
        return render_template('index.html',p=prediction)


if __name__ == "__main__":
    app.run(debug=True)