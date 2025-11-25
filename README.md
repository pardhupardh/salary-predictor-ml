💼 Salary Prediction Web App
A simple & interactive Streamlit-based ML application

⭐ Overview
This project is a Machine Learning–powered Salary Prediction Web Application built using Python, Streamlit, and Scikit-Learn.
Users can input their Years of Experience, Test Score, and Interview Score, and the app predicts the expected salary instantly.

This project demonstrates:
🔹 ML model training & serialization
🔹 Clean code structure
🔹 Streamlit UI development
🔹 Deployment on Streamlit Cloud
🔹 GitHub project setup best practices

🚀 Features
✔️ Real-time salary prediction
✔️ Clean & minimal web UI using Streamlit
✔️ ML model trained using Linear Regression
✔️ Lightweight & fast deployment
✔️ Portable — runs on any system

🧠 Machine Learning Model
Algorithm: Linear Regression
Library: scikit-learn

Serialized model: model.pkl / model.joblib
Inputs:
Years of Experience
Test Score
Interview Score

🏗 Project Structure
Salary_Prediction_App/
│── app.py                     # Streamlit frontend
│── model.pkl                  # Trained ML model
│── requirements.txt           # Dependencies
│── README.md                  # Project documentation
│── .gitignore                 # Ignored files
└── data/
    └── dataset.csv            # Training data

📦 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the environment
Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Run the application
streamlit run app.py

🌐 Deployment (Streamlit Cloud)
Step-by-step:
Push all project files to GitHub
Go to https://share.streamlit.io
Login using GitHub
Click Create New App
Select your repository
Choose your branch
Set the Main file → app.py
Click Deploy 🚀
Your app will be hosted live automatically.

🗂 .gitignore Used
venv/
__pycache__/
*.pyc
*.pkl
*.joblib
.DS_Store
.env

📑 Requirements
Example requirements.txt:
streamlit
pandas
numpy
scikit-learn
joblib

📝 Future Enhancements
Add authentication
Add more features (Domain, Education Level, Company Size)
Deploy using Docker
Replace Linear Regression with a more powerful ML model

✨ Author
Pardhasaradhi
📧 pardhuaggunna@gmail.com
🔗 GitHub: https://github.com/pardhupardh
