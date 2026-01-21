import streamlit as st
from predict import predict_text

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Text Classification System",
    layout="centered"
)

# ---------------- Initialize Session State ----------------
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# ---------------- Helper Function ----------------
def get_text_type(word_count):
    if word_count < 20:
        return "Short Text"
    elif word_count <= 80:
        return "Medium Text"
    else:
        return "Long Text"

# ---------------- Title & Description ----------------
st.title("Text Classification System")
st.write(
    "This application classifies input text using data mining and machine "
    "learning techniques. It also analyzes the text length and structure."
)

st.divider()

# ---------------- Text Input ----------------
st.session_state.input_text = st.text_area(
    "Enter Text for Classification",
    value=st.session_state.input_text,
    height=180,
    placeholder="Type or paste text here..."
)

# ---------------- Text Analysis ----------------
if st.session_state.input_text.strip():
    words = st.session_state.input_text.split()
    word_count = len(words)
    char_count = len(st.session_state.input_text)
    text_type = get_text_type(word_count)

    col1, col2, col3 = st.columns(3)
    col1.metric("Word Count", word_count)
    col2.metric("Character Count", char_count)
    col3.metric("Text Type", text_type)

st.divider()

# ---------------- Buttons ----------------
col1, col2 = st.columns(2)

with col1:
    classify_btn = st.button("Classify Text")

with col2:
    clear_btn = st.button("Clear Text")

# ---------------- Clear Button Logic ----------------
if clear_btn:
    st.session_state.input_text = ""

# ---------------- Prediction Output ----------------
if classify_btn:
    if st.session_state.input_text.strip() == "":
        st.warning("Please enter valid text before classification.")
    else:
        label, score = predict_text(st.session_state.input_text)

        st.subheader("Prediction Result")
        st.success(f"Predicted Class: {label}")

        st.write("Confidence Level")
        st.progress(min(score, 1.0))

        st.info(f"Confidence Score: {round(score, 2)}")

        st.subheader("Text Summary")
        st.write(
            f"- **Text Type:** {text_type}\n"
            f"- **Total Words:** {word_count}\n"
            f"- **Total Characters:** {char_count}"
        )

        st.subheader("Result Interpretation")
        st.write(
            f"The model classifies the given **{text_type.lower()}** as "
            f"**{label}** with a confidence score of **{round(score, 2)}**. "
            "Higher confidence indicates stronger prediction reliability."
        )

st.divider()
st.caption("Text Classification Project | Data Mining & Machine Learning")
