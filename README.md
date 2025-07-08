# 📄 Resume Screening App

A Streamlit-based web application that classifies uploaded resumes into appropriate job categories using Natural Language Processing (NLP) and a machine learning classifier.

---

## Features

- Upload resumes in `.txt` or `.pdf` format.
- Automatically cleans and processes text using NLP techniques.
- Predicts the most suitable job role from 20+ categories.
- Interactive and intuitive Streamlit web interface.

---

##  Technologies Used

- **Python**
- **Streamlit**
- **NLTK** – for text preprocessing
- **Scikit-learn** – for TF-IDF vectorization and classification
- **Pickle** – for model serialization

---

##  Project Structure

```
├── app.py                  # Main Streamlit app
├── clf_compressed.pkl                 # Trained ML classifier
├── tfidf.pkl               # TF-IDF vectorizer
├── Resume_Screening.ipynb  # Notebook
└── README.md               # Project documentation
```

---

##  How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Kahkashan2708/Resume-Analyser-Application.git
cd resume-screening-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

---

##  Input Format

Upload resumes in:
- `.txt` format
- `.pdf` format (UTF-8 or Latin-1 encoded)

---

##  Sample Output

Once a resume is uploaded, the app displays:
```
**Predicted Category:**  Data Science
```

Other possible categories:
-  HR
-  Java Developer
-  Business Analyst
- SAP Developer
-  Python Developer
- ...and more!

---

##  Contact

**Kahkashan Manzoor**  
[Email](mailto:kahkashanmanzoor06@gmail.com) • [LinkedIn](https://www.linkedin.com/in/kahkashan-manzoor-663384287/) • [GitHub](https://github.com/Kahkashan2708) • [Kaggle](https://www.kaggle.com/kashishmanzoor)

---

## ⭐ Star the repo if you find it useful!


