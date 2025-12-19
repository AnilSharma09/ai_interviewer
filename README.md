# AI Interviewer

## Project Overview
AI Interviewer is an NLP-based application designed to automate the initial screening process of technical interviews. By analyzing a Job Description (JD), the system generates relevant technical questions and evaluates candidate answers using semantic similarity matching.

## Technologies Used
- **Python 3.x**
- **Streamlit**: For the web interface.
- **spaCy**: For Natural Language Processing and keyword extraction.
- **Sentence-Transformers**: For semantic similarity evaluation.
- **scikit-learn / NumPy**: For numerical operations.

## Features
1. **Job Description Parsing**: Extracts key technical skills and nouns from the text.
2. **Automated Question Generation**: Creates context-aware questions based on extracted skills.
3. **Smart Answer Evaluation**: Scores answers (0-10) based on relevance and definition matching.
4. **Instant Feedback**: Provides qualitative feedback (Good/Average/Needs Improvement).
5. **Report Generation**: Export results to CSV.

## How It Works
1. **Input**: User pastes a Job Description.
2. **Process**: The system identifies keywords (e.g., "Python", "SQL").
3. **Generate**: It populates questions using predefined templates (e.g., "Explain the concept of Python...").
4. **Answer**: Candidate types their responses.
5. **Evaluate**: The system compares the answer embedding with a generated anchor context to determine relevance.

## Installation Steps
1. Navigate to the project directory:
   ```bash
   cd ai_interviewer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download spaCy model (if not automatically handled):
   ```bash
   python -m spacy download en_core_web_sm
   ```

## How to Run
Run the Streamlit application:
```bash
streamlit run app.py
```
The application will open in your default browser at `http://localhost:8501`.

## Sample Output
*(See the running application for live demos)*
- **JD Input**: "Looking for a React developer..."
- **Generated Q**: "What are the key advantages of using React?"
- **Answer**: "React is a JS library for building UIs..."
- **Evaluation**: Score: 8/10, Feedback: "Excellent!"
