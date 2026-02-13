import streamlit as st
import pickle
import re
import subprocess
import tempfile
import os

# ==============================
# LOAD SAVED MODEL
# ==============================

MODEL_PATH = "models/error_classifier.pkl"
VECTORIZER_PATH = "models/error_vectorizer.pkl"

error_model = pickle.load(open(MODEL_PATH, "rb"))
error_vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))

# ==============================
# EXECUTION ENGINE
# ==============================

def execute_code(code):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        filename = f.name

    result = subprocess.run(
        ["python", filename],
        capture_output=True,
        text=True
    )

    return result.stderr.strip()

# ==============================
# PREDICT ERROR TYPE
# ==============================

def predict_error_type(error_text):
    vec = error_vectorizer.transform([error_text])
    return error_model.predict(vec)[0]

# ==============================
# INTELLIGENT FIX ENGINE
# ==============================

def generate_fix(error_type, error_message):

    suggestion_match = re.search(r"Did you mean: '(.+?)'\?", error_message)
    if suggestion_match:
        suggestion = suggestion_match.group(1)
        return f"It looks like a typo. Did you mean '{suggestion}'?"

    if error_type == "SyntaxError":
        if "unterminated string literal" in error_message:
            return "Add a closing quotation mark."
        if "was never closed" in error_message:
            return "Close the missing bracket or parenthesis."
        if "expected ':'" in error_message:
            return "Add ':' at the end of the statement."
        return "Check syntax carefully."

    if error_type == "IndentationError":
        if "expected an indented block" in error_message:
            return "Indent the next line after the loop or function."
        if "unexpected indent" in error_message:
            return "Remove extra indentation."
        return "Fix indentation using consistent 4 spaces."

    if error_type == "NameError":
        match = re.search(r"name '(.+?)' is not defined", error_message)
        if match:
            variable = match.group(1)
            return f"The variable '{variable}' is not defined. Define it before using."
        return "Make sure all variables are defined."

    if error_type == "TypeError":
        if "concatenate str" in error_message:
            return "Convert integer using str() before concatenation."
        if "unsupported operand type" in error_message:
            return "Ensure operands are compatible types."
        if "positional argument" in error_message:
            return "Check number of arguments passed."
        return "Check data types used."

    if error_type == "ZeroDivisionError":
        return "You are dividing by zero. Add a condition before division."

    if error_type == "IndexError":
        return "List index is out of range. Check list length."

    if error_type == "KeyError":
        return "Dictionary key does not exist."

    if error_type == "AttributeError":
        return "Object does not have this attribute."

    if error_type == "ValueError":
        return "Invalid value passed to function."

    if error_type == "ModuleNotFoundError":
        return "Install required module using pip."

    if error_type == "FileNotFoundError":
        return "Check file path. File may not exist."

    return "Review your code carefully."

# ==============================
# STREAMLIT UI
# ==============================

st.set_page_config(page_title="Intelligent Error Analyzer")

st.title("🧠 Intelligent Python Error Analyzer")

code_input = st.text_area("Enter your Python code below:", height=200)

if st.button("Analyze Code"):

    if not code_input.strip():
        st.warning("Please enter some code.")
    else:
        error_log = execute_code(code_input)

        if not error_log:
            st.success("✅ Code executed successfully!")
        else:
            error_type = predict_error_type(error_log)
            fix = generate_fix(error_type, error_log)

            st.error("⚠️ Error Detected")
            st.code(error_log)

            st.subheader
            ("Predicted Error Type:")
            st.write(error_type)

            st.subheader("Suggested Fix:")
            st.write(fix)
