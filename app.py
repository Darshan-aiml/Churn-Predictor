from flask import Flask, request, jsonify
import pandas as pd
from pycaret.classification import load_model, predict_model
from flask_cors import CORS

app = Flask(__name__)   
CORS(app)               


model = load_model('best_churn_model')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Convert request JSON to DataFrame
        input_data = request.get_json()
        df = pd.DataFrame([input_data])

        # Predict
        predictions = predict_model(model, data=df)

        # Prepare response
        output = {
            "prediction": predictions["prediction_label"].iloc[0],
            "confidence": round(predictions["prediction_score"].iloc[0], 2)
        }
        return jsonify(output)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)    
    
