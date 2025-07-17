📊 AutoML Churn Prediction Web App

This is a full-stack web application that predicts customer churn using a PyCaret AutoML pipeline.
It consists of a Flask API backend and a React frontend.

🚀 Features
📦 Backend built using Flask + PyCaret
🖥️ Frontend built with React (Vite)
🔮 Predicts customer churn based on user input
🔗 RESTful API integration
☁️ Deployable on platforms like Railway, Render, or AWS
🧠 Tech Stack
Layer	  Technology
Backend	 Python, Flask, PyCaret
Frontend	React.js (Vite)
ML Model	PyCaret AutoML
Hosting	Railway (or any other cloud)
📁 Project Structure
automl-churn-pipeline/
├── app.py               # Flask backend
├── best_churn_model.pkl # Trained PyCaret model
├── requirements.txt     # Python dependencies
├── client/              # React frontend (Vite)
│   ├── index.html
│   ├── vite.config.js
│   └── src/
│       └── App.jsx
└── dist/                # Production build of React app (auto-generated)
⚙️ Setup Instructions
1. Clone the repository

git clone https://github.com/your-username/automl-churn-pipeline.git
cd automl-churn-pipeline
2. Install Python dependencies

pip install -r requirements.txt
3. Train or load PyCaret model (if not already)

# If not present, generate best_churn_model.pkl using PyCaret
4. Build the React frontend

cd client
npm install
npm run build
This generates a dist/ folder used by Flask to serve static files.
5. Run Flask server

cd ..
python3 app.py
Visit the app at: http://localhost:5000

📬 API Endpoint
POST /predict
Send customer data JSON to this endpoint.

Example request (via Postman or curl):

curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "customerID": "12345",
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "Yes",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.35,
    "TotalCharges": 845.5
}'
🧪 Sample Prediction Response
{
  "prediction": "Yes",
  "confidence": 0.84
}
🌐 Deployment
For deployment:

Push the entire project (Flask + built React) to a GitHub repo
Deploy on Railway, Render, or Fly.io
Ensure dist/ is served by Flask in app.py:
app = Flask(__name__, static_folder="dist", static_url_path="/")

@app.route("/")
def index():
    return app.send_static_file("index.html")
