from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('first.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        print("Received data:", data)  # Add this line to print the received data
        prediction = model.predict([data])
        return f'The predicted class is: {prediction[0]}'
    except Exception as e:
        return f'An error occurred: {str(e)}'


if __name__ == '__main__':
    app.run()
