import sys
import os

# Ensure we can import modules from current directory
sys.path.append(os.getcwd())

print("Testing imports...")
try:
    from question_generator import QuestionGenerator
    from answer_evaluator import AnswerEvaluator
    print("Imports successful.")
except ImportError as e:
    print(f"Import failed: {e}")
    sys.exit(1)

print("Testing Question Generator...")
try:
    gen = QuestionGenerator()
    jd = "We need a Software Engineer with experience in Python, Flask, and React."
    questions = gen.generate_questions(jd, num_questions=3)
    print(f"Generated {len(questions)} questions.")
    for q in questions:
        print(f" - {q['question']} (Keyword: {q['keyword']})")
except Exception as e:
    print(f"Question Generator failed: {e}")
    # Don't exit, try evaluator

print("\nTesting Answer Evaluator...")
try:
    evaluator = AnswerEvaluator()
    # Mock data
    question = "Can you explain the concept of Python and how it is used?"
    keyword = "Python"
    ans_good = "Python is a versatile programming language used for web development and data science."
    ans_bad = "I like apples."
    
    res_good = evaluator.evaluate_answer(question, keyword, ans_good)
    res_bad = evaluator.evaluate_answer(question, keyword, ans_bad)
    
    print(f"Score for good answer: {res_good['score']} (Feedback: {res_good['feedback']})")
    print(f"Score for bad answer: {res_bad['score']} (Feedback: {res_bad['feedback']})")
    
    if res_good['score'] > res_bad['score']:
        print("Scoring logic check passed.")
    else:
        print("Scoring logic check failed.")

except Exception as e:
    print(f"Answer Evaluator failed: {e}")

print("\nVerification Complete.")
