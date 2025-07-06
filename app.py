import streamlit as st
import pickle
import re
import nltk

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load models
clf = pickle.load(open('clf.pkl', "rb"))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

# Resume cleaning function
def CleanResume(txt):
    txt = re.sub(r'https?://\S+|www\.\S+', '', txt)
    txt = re.sub(r'\bRT\b|\bcc\b', '', txt)
    txt = re.sub(r'#\S+', '', txt)
    txt = re.sub(r'@\S+', '', txt)
    txt = re.sub(r'[^\x00-\x7f]', ' ', txt)
    txt = re.sub(r'[!"#$%&\'()*+,-/:;<=>?@\[\\\]^_{|}~]', '', txt)
    txt = re.sub(r'\s+', ' ', txt)
    return txt.strip()

# Category mapping
category_mapping = {
    6: '🧠 Data Science',
    12: '💼 HR',
    0: '⚖️ Advocate',
    1: '🎨 Arts',
    24: '🖥️ Web Designing',
    16: '🔧 Mechanical Engineer',
    22: '📈 Sales',
    14: '🏋️ Health & Fitness',
    5: '🏗️ Civil Engineer',
    15: '☕ Java Developer',
    4: '📊 Business Analyst',
    21: '🛠️ SAP Developer',
    2: '🤖 Automation Testing',
    11: '⚡ Electrical Engineer',
    18: '🧩 Operations Manager',
    20: '🐍 Python Developer',
    8: '🚀 DevOps Engineer',
    17: '🔐 Network Security Engineer',
    19: '📋 PMO',
    7: '🗄️ Database',
    13: '🌀 Hadoop',
    10: '🔄 ETL Developer',
    9: '🌐 DotNet Developer',
    3: '⛓️ Blockchain',
    23: '🧪 Testing'
}

# Streamlit Web App
def main():
    st.set_page_config(page_title="Resume Screening App", layout="centered")
    st.title("📄 Resume Screening App")

    with st.sidebar:
        st.header(" Instructions")
        st.markdown("""
        - Upload your resume in `.txt` or `.pdf` format.
        - The app will predict the most suitable **job role**.
        """)

    uploaded_file = st.file_uploader(" Upload Your Resume", type=['txt', 'pdf'])

    if uploaded_file is not None:
        with st.spinner(" Analyzing your resume..."):
            try:
                resume_bytes = uploaded_file.read()
                resume_text = resume_bytes.decode('utf-8')
            except UnicodeDecodeError:
                resume_text = resume_bytes.decode('latin-1')

            cleaned_resume = CleanResume(resume_text)
            input_features = tfidf.transform([cleaned_resume])
            prediction_id = clf.predict(input_features)[0]
            category_name = category_mapping.get(prediction_id, " UNKNOWN")

            st.success(f" **Predicted Category:** {category_name}")

            
# Run the app
if __name__ == "__main__":
    main()


