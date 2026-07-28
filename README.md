# 🤖 AI Interviewer – NLP-Based Technical Interview Screening System

An AI-powered interview assistant that automates the first round of technical interviews by analyzing a Job Description (JD), generating relevant interview questions, and evaluating candidate responses using Natural Language Processing (NLP) and semantic similarity.

---

## 📌 Overview

AI Interviewer helps recruiters and hiring teams conduct initial technical screening efficiently. Instead of manually preparing interview questions, the system extracts important technical skills from a Job Description, generates customized interview questions, and evaluates candidate answers based on their semantic meaning rather than simple keyword matching.

This project demonstrates the practical application of **Natural Language Processing (NLP)** and **Sentence Embeddings** in recruitment automation.

---

## ✨ Key Features

- 📄 **Job Description Analysis**
  - Extracts important technical skills and keywords from a JD.
  - Identifies technologies, programming languages, frameworks, and concepts.

- ❓ **Automatic Question Generation**
  - Generates technical interview questions dynamically.
  - Uses predefined templates combined with extracted skills.

- 🧠 **Semantic Answer Evaluation**
  - Evaluates candidate answers using Sentence Transformers.
  - Measures semantic similarity instead of exact keyword matching.

- 📊 **Automated Scoring**
  - Scores answers on a scale of **0–10**.
  - Provides qualitative feedback.

- 💬 **Instant Feedback**
  - Excellent
  - Good
  - Average
  - Needs Improvement

- 📁 **Result Export**
  - Saves interview results to CSV for future analysis.

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core Programming Language |
| Streamlit | Interactive Web Application |
| spaCy | NLP & Keyword Extraction |
| Sentence-Transformers | Semantic Similarity |
| NumPy | Numerical Operations |
| scikit-learn | Machine Learning Utilities |
| Pandas | Data Handling |

---

# 🧠 Project Workflow

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

# 📂 Project Structure

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

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/AI-Interviewer.git
```

```bash
cd AI-Interviewer
```

---

## Create a Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Download spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

After running the command, open your browser and visit:

```
http://localhost:8501
```

---

# 🚀 How It Works

### Step 1

Paste a Job Description.

Example:

```
Looking for a Python Developer with knowledge of SQL,
Machine Learning, Flask, REST APIs, and Git.
```

↓

### Step 2

The NLP engine extracts important technical skills.

Example:

```
Python
SQL
Machine Learning
REST API
Git
Flask
```

↓

### Step 3

The system automatically generates interview questions.

Example:

```
Explain Python.

What is SQL?

How do REST APIs work?

What is Flask?

Explain Machine Learning.
```

↓

### Step 4

Candidate submits answers.

↓

### Step 5

Sentence Transformer converts both expected answer and candidate answer into embeddings.

↓

### Step 6

Semantic similarity score is calculated.

↓

### Step 7

Final score and feedback are generated.

Example:

| Score | Feedback |
|-------|----------|
| 9/10 | Excellent |
| 8/10 | Good |
| 6/10 | Average |
| 4/10 | Needs Improvement |

---

# 📈 Sample Interview

### Job Description

```text
Looking for a React Developer with knowledge of JavaScript,
REST APIs, Git, and HTML/CSS.
```

---

### Generated Question

```
What are the advantages of using React?
```

---

### Candidate Answer

```
React is a JavaScript library used for building reusable UI
components and creating fast single-page applications.
```

---

### Evaluation

```text
Semantic Similarity : 0.87

Score : 9/10

Feedback :
Excellent understanding of the concept.
```

---

# 📊 Evaluation Strategy

The application evaluates responses using semantic similarity instead of exact keyword matching.

Evaluation considers:

- Concept correctness
- Context relevance
- Technical terminology
- Semantic meaning
- Overall completeness

This approach allows candidates to answer naturally without needing exact wording.

---

# 🎯 Use Cases

- Technical Recruitment
- HR Screening
- Campus Placements
- Coding Bootcamps
- Internship Hiring
- Mock Technical Interviews
- Learning & Self-Assessment

---

# 🔮 Future Enhancements

- Voice-based interviews
- AI-generated follow-up questions
- Resume parsing
- LLM-powered answer evaluation
- Multi-language support
- PDF report generation
- Authentication system
- Database integration
- Video interview support
- Performance analytics dashboard

---

# 📸 Screenshots

Add application screenshots here.

```text
screenshots/
│
├── home.png
├── interview.png
├── report.png
└── result.png
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Anil Sharma**

B.Tech – Artificial Intelligence & Data Science


---

## ⭐ If you found this project helpful, please consider giving it a Star!
