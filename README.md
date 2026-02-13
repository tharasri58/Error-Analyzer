
# 🧠 Intelligent Python Error Analyzer

An intelligent hybrid system that analyzes Python code, detects runtime and syntax errors,
predicts the error type using Machine Learning, and generates human-readable fix suggestions
using a rule-based enhancement engine.

---

## 🚀 Project Overview

The Intelligent Python Error Analyzer assists programmers by:

- Executing user-submitted Python code
- Capturing runtime and syntax errors
- Predicting the error type using a trained ML classifier
- Generating intelligent, context-aware fix suggestions
- Providing an interactive Streamlit web interface

---

## 🏗️ Architecture

User Code  
↓  
Execution Engine (Python Subprocess)  
↓  
Error Log Captured  
↓  
ML Model → Predict Error Type  
↓  
Hybrid Fix Engine (Pattern + Rules)  
↓  
Suggested Fix Output  

---

## 📂 Project Structure

intelligent-error-analyzer/
│
├── models/
│   ├── error_classifier.pkl
│   └── error_vectorizer.pkl
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── dataset/

---

## 🧠 Supported Error Types

- NameError
- TypeError
- ZeroDivisionError
- IndexError
- KeyError
- AttributeError
- ValueError
- IndentationError
- SyntaxError
- ModuleNotFoundError
- FileNotFoundError
- UnboundLocalError

---

## 📊 Machine Learning Model

- Algorithm: Logistic Regression
- Feature Extraction: TF-IDF Vectorizer (n-grams)
- Dataset Source: StackOverflow Python Questions (Kaggle)
- Error Model Accuracy: ~99%

The ML model predicts only the error type.  
Fix suggestions are generated using a hybrid rule-based engine.

---

## 🖥️ Installation

### 1️⃣ Clone Repository

git clone <your-repo-url>  
cd intelligent-error-analyzer  

### 2️⃣ Create Virtual Environment

python -m venv venv  
venv\Scripts\activate  

### 3️⃣ Install Dependencies

pip install -r requirements.txt  

---

## ▶️ Run the Application

streamlit run streamlit_app.py  

Then open:  
http://localhost:8501  

---

## 🧪 Example Test Cases

Example 1 – Typo:

prin("Hello")

Output:
- NameError
- Suggestion: Did you mean 'print'?

Example 2 – Division by Zero:

5/0

Output:
- ZeroDivisionError
- Suggestion: Add condition before division.

Example 3 – Type Mismatch:

a = "5" + 5

Output:
- TypeError
- Suggestion: Convert integer using str() before concatenation.

---

## 🎓 Academic Value

This project demonstrates:

- Natural Language Processing (TF-IDF)
- Supervised Machine Learning
- Hybrid System Design
- Error Handling Pipeline
- Web Application Deployment (Streamlit)

---

## 👩‍💻 Author

Tharasri Sakthivel  
MCA (AI & ML)
