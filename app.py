import streamlit as st
import pandas as pd
from question_generator import QuestionGenerator
from answer_evaluator import AnswerEvaluator

# Page Configuration
st.set_page_config(
    page_title="AI Technical Interviewer",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stTextArea textarea {
        background-color: #000000;
        border: 1px solid #ddd;
    }
    h1 {
        color: #2c3e50;
    }
    .question-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("🤖 AI Technical Interviewer")
    st.caption("Practice your technical interview skills with AI analysis.")

    # Initialize Logic Classes
    try:
        # Lazy initialization to avoid reloading models on every rerun if possible
        # but Streamlit runs top-down. Storing in session_state works.
        if 'generator' not in st.session_state:
            with st.spinner("Loading AI Models..."):
                st.session_state.generator = QuestionGenerator()
                st.session_state.evaluator = AnswerEvaluator()
                st.success("Models Loaded Successfully!")
    except RuntimeError as e:
        st.error(f"System Error: {e}")
        st.info("Please ensure 'requirements.txt' contains the correct spaCy model URL.")
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        st.stop()

    # Sidebar - Configuration
    with st.sidebar:
        st.header("Settings")
        role = st.selectbox(
            "Select Interview Role",
            ["Python Developer", "React Frontend", "Machine Learning Engineer", "General Developer"]
        )
        num_questions = st.slider("Number of Questions", 1, 5, 3)
        
        if st.button("Start New Interview"):
            # Generate new questions and reset state
            st.session_state.questions = st.session_state.generator.generate_questions(role, num_questions)
            st.session_state.answers = {} # Reset answers
            st.session_state.evaluated = False
            st.session_state.current_role = role
            st.rerun()

    # Main Interview Logic
    if 'questions' not in st.session_state:
        st.info("👈 Please select a role and click 'Start New Interview' to begin.")
    else:
        st.subheader(f"Role: {st.session_state.get('current_role', role)}")
        
        with st.form("interview_form"):
            user_inputs = {}
            for i, q_data in enumerate(st.session_state.questions):
                st.markdown(f"### Q{i+1}: {q_data['question']}")
                # Use a unique key for each text area
                user_inputs[i] = st.text_area(
                    "Your Answer:", 
                    key=f"q_{i}", 
                    height=100,
                    placeholder="Type your explanation here..."
                )
            
            submitted = st.form_submit_button("Submit & Evaluate")
            
            if submitted:
                st.session_state.answers = user_inputs
                st.session_state.evaluated = True

        # Evaluation Results
        if st.session_state.get('evaluated', False):
            st.divider()
            st.header("📝 Evaluation Report")
            
            total_score = 0
            
            for i, q_data in enumerate(st.session_state.questions):
                user_ans = st.session_state.answers.get(i, "")
                score, feedback, missing = st.session_state.evaluator.evaluate_answer(
                    user_ans, 
                    q_data['keywords']
                )
                total_score += score
                
                with st.expander(f"Result for Q{i+1} (Score: {score:.0f}/100)"):
                    st.write(f"**Question:** {q_data['question']}")
                    st.write(f"**Your Answer:** {user_ans if user_ans else '*(No Answer)*'}")
                    
                    if score > 70:
                        st.success(feedback)
                    elif score > 40:
                        st.warning(feedback)
                    else:
                        st.error(feedback)
                        
                    if missing:
                        st.write("**Keywords missed:**")
                        st.caption(", ".join(missing))
            
            avg_score = total_score / len(st.session_state.questions)
            st.metric("Overall Interview Score", f"{avg_score:.1f} / 100")
            
            if avg_score > 80:
                st.balloons()
            
if __name__ == "__main__":
    main()
