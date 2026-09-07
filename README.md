<div align="center">

# 🤖 AI Interviewer
### NLP-Based Technical Interview Screening System

*An AI-powered interview assistant that automates the first round of technical interviews by analyzing a Job Description, generating relevant questions, and evaluating candidate responses using NLP and semantic similarity.*

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📌 Overview

AI Interviewer helps recruiters and hiring teams conduct initial technical screening efficiently. Instead of manually preparing interview questions, the system extracts important technical skills from a Job Description, generates customized interview questions, and evaluates candidate answers based on their **semantic meaning** rather than simple keyword matching.

This project demonstrates the practical application of **Natural Language Processing (NLP)** and **Sentence Embeddings** in recruitment automation.

---

## ✨ Key Features

| | Feature | Description |
|---|---|---|
| 📄 | **Job Description Analysis** | Extracts key technical skills, technologies, frameworks, and concepts from a JD. |
| ❓ | **Automatic Question Generation** | Dynamically generates technical interview questions using templates + extracted skills. |
| 🧠 | **Semantic Answer Evaluation** | Evaluates candidate answers with Sentence Transformers — meaning over keywords. |
| 📊 | **Automated Scoring** | Scores answers on a 0–10 scale with qualitative feedback. |
| 💬 | **Instant Feedback** | Excellent · Good · Average · Needs Improvement |
| 📁 | **Result Export** | Saves interview results to CSV for future analysis. |

---

## 🛠 Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)
![Sentence Transformers](https://img.shields.io/badge/Sentence--Transformers-FFCA28?style=for-the-badge&logo=huggingface&logoColor=black)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

</div>

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language |
| **Streamlit** | Interactive web application |
| **spaCy** | NLP & keyword extraction |
| **Sentence-Transformers** | Semantic similarity |
| **NumPy** | Numerical operations |
| **scikit-learn** | Machine learning utilities |
| **Pandas** | Data handling |

---

## 🧠 Project Workflow

```text
            Job Description
                    │
                    ▼
      NLP Keyword Extraction (spaCy)
                    │
                    ▼
      Technical Skills Identification
                    │
                    ▼
      Automatic Question Generation
                    │
                    ▼
      Candidate Answers
                    │
                    ▼
 Sentence Embedding Generation
                    │
                    ▼
 Semantic Similarity Comparison
                    │
                    ▼
      Score + Feedback Generation
                    │
                    ▼
          CSV Report Export
```

---

## 📂 Project Structure

```text
AI-Interviewer/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Required Python libraries
├── utils.py                # Helper functions
├── evaluator.py            # Answer evaluation logic
├── question_generator.py   # Dynamic question generation
├── data/
│   ├── templates.csv
│   └── definitions.csv
│
├── reports/
│   └── interview_results.csv
│
├── assets/
│   └── logo.png
│
└── README.md
```

> Folder names may vary depending on your implementation.

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/AI-Interviewer.git
cd AI-Interviewer
```

**2. Create a virtual environment** *(optional)*

<table>
<tr><th>Windows</th><th>Linux / macOS</th></tr>
<tr>
<td>

```bash
python -m venv venv
venv\Scripts\activate
```

</td>
<td>

```bash
python3 -m venv venv
source venv/bin/activate
```

</td>
</tr>
</table>

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Download the spaCy language model**

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open your browser and visit:

```
http://localhost:8501
```

---

## 🚀 How It Works

| Step | Action |
|---|---|
| **1** | Paste a Job Description — e.g. *"Looking for a Python Developer with knowledge of SQL, Machine Learning, Flask, REST APIs, and Git."* |
| **2** | The NLP engine extracts key skills: `Python`, `SQL`, `Machine Learning`, `REST API`, `Git`, `Flask` |
| **3** | The system auto-generates interview questions: *"Explain Python."*, *"What is SQL?"*, *"How do REST APIs work?"* |
| **4** | Candidate submits answers |
| **5** | Sentence Transformer converts expected & candidate answers into embeddings |
| **6** | Semantic similarity score is calculated |
| **7** | Final score and feedback are generated |

**Scoring guide:**

| Score | Feedback |
|:---:|---|
| 9–10 | 🟢 Excellent |
| 7–8 | 🔵 Good |
| 5–6 | 🟡 Average |
| < 5 | 🔴 Needs Improvement |

---

## 📈 Sample Interview

**Job Description**
```text
Looking for a React Developer with knowledge of JavaScript,
REST APIs, Git, and HTML/CSS.
```

**Generated Question**
```
What are the advantages of using React?
```

**Candidate Answer**
```
React is a JavaScript library used for building reusable UI
components and creating fast single-page applications.
```

**Evaluation**

| Metric | Value |
|---|---|
| Semantic Similarity | 0.87 |
| Score | 9 / 10 |
| Feedback | Excellent understanding of the concept |

---

## 📊 Evaluation Strategy

The application evaluates responses using **semantic similarity** instead of exact keyword matching. Evaluation considers:

- ✅ Concept correctness
- ✅ Context relevance
- ✅ Technical terminology
- ✅ Semantic meaning
- ✅ Overall completeness

This approach allows candidates to answer naturally without needing exact wording.

---

## 🎯 Use Cases

<div align="center">

`Technical Recruitment` `HR Screening` `Campus Placements` `Coding Bootcamps`
`Internship Hiring` `Mock Technical Interviews` `Learning & Self-Assessment`

</div>

---

## 🔮 Future Enhancements

- [ ] Voice-based interviews
- [ ] AI-generated follow-up questions
- [ ] Resume parsing
- [ ] LLM-powered answer evaluation
- [ ] Multi-language support
- [ ] PDF report generation
- [ ] Authentication system
- [ ] Database integration
- [ ] Video interview support
- [ ] Performance analytics dashboard

---

## 📸 Screenshots

> Add application screenshots here.

```text
screenshots/
│
├── home.png
├── interview.png
├── report.png
└── result.png
```

---

## 🤝 Contributing

Contributions are welcome!

```bash
# 1. Fork the repository

# 2. Create a new branch
git checkout -b feature-name

# 3. Commit your changes
git commit -m "Add new feature"

# 4. Push to GitHub
git push origin feature-name

# 5. Open a Pull Request
```

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

## 👨‍💻 Author

**Anil Sharma**
B.Tech – Artificial Intelligence & Data Science

⭐ **If you found this project helpful, please consider giving it a Star!**

</div>
