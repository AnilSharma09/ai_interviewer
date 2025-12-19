import streamlit as st
from question_generator import QuestionGenerator
from answer_evaluator import AnswerEvaluator
import pandas as pd

# Page config
st.set_page_config(page_title="AI Interviewer", layout="wide")

# Custom CSS for UI
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stTextArea textarea {
        background-color: #ffffff;
    }
    .score-card {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .good { background-color: #d4edda; color: #155724; }
    .average { background-color: #fff3cd; color: #856404; }
    .poor { background-color: #f8d7da; color: #721c24; }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🤖 AI Interviewer")
st.markdown("### NLP Based Interview Question Generator and Answer Evaluator")

# Initialize modules (cached to avoid reload)
@st.cache_resource
def get_generator():
    return QuestionGenerator()

@st.cache_resource
def get_evaluator():
    return AnswerEvaluator()

generator = get_generator()
evaluator = get_evaluator()

# Session State for Questions and Answers
if 'questions' not in st.session_state:
    st.session_state['questions'] = []
if 'answers' not in st.session_state:
    st.session_state['answers'] = {}
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

# Sidebar or Input Section
with st.container():
    st.subheader("1. Job Description")
    jd_input = st.text_area("Paste the Job Description here:", height=150, placeholder="e.g. We are looking for a Data Scientist proficient in Python, SQL, and Machine Learning...")
    
    if st.button("Generate Interview Questions"):
        if jd_input.strip():
            with st.spinner("Extracting keywords and generating questions..."):
                questions = generator.generate_questions(jd_input)
                st.session_state['questions'] = questions
                st.session_state['answers'] = {i: "" for i in range(len(questions))}
                st.session_state['submitted'] = False
            st.success(f"Generated {len(questions)} questions based on the JD!")
        else:
            st.warning("Please enter a Job Description first.")

# Question & Answer Section
if st.session_state['questions']:
    st.subheader("2. Interview Session")
    
    with st.form("interview_form"):
        for i, item in enumerate(st.session_state['questions']):
            st.markdown(f"**Q{i+1}: {item['question']}**")
            st.session_state['answers'][i] = st.text_area(f"Your Answer for Q{i+1}", key=f"ans_{i}", height=100)
            st.markdown("---")
        
        submit_button = st.form_submit_button("Submit Answers")
        
        if submit_button:
            st.session_state['submitted'] = True

# Evaluation Section
if st.session_state['submitted']:
    st.subheader("3. Evaluation Report")
    
    total_score = 0
    max_score = len(st.session_state['questions']) * 10
    results_data = []

    for i, item in enumerate(st.session_state['questions']):
        user_ans = st.session_state['answers'].get(i, "")
        result = evaluator.evaluate_answer(item['question'], item['keyword'], user_ans)
        
        score = result['score']
        feedback = result['feedback']
        total_score += score
        
        # Determine CSS class for styling
        status_class = "poor"
        if score >= 8: status_class = "good"
        elif score >= 5: status_class = "average"
        
        st.markdown(f"""
        <div class="score-card {status_class}">
            <h4>Q{i+1}: {item['question']}</h4>
            <p><b>Your Answer:</b> {user_ans}</p>
            <p><b>Score:</b> {score}/10 | <b>Feedback:</b> {feedback}</p>
        </div>
        """, unsafe_allow_html=True)
        
        results_data.append([item['question'], user_ans, score, feedback])

    # Final Summary
    st.markdown("### Performance Summary")
    percentage = (total_score / max_score) * 100
    st.metric("Total Score", f"{total_score}/{max_score}", f"{percentage:.1f}%")
    
    if percentage >= 80:
        st.balloons()
        st.success("Result: Excellent! You are a strong candidate.")
    elif percentage >= 50:
        st.info("Result: Average. Good foundation but needs polish.")
    else:
        st.error("Result: Needs Improvement. Focus more on key concepts.")

    # Download Results
    df = pd.DataFrame(results_data, columns=["Question", "Answer", "Score", "Feedback"])
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Report Results CSV", csv, "interview_report.csv", "text/csv")

