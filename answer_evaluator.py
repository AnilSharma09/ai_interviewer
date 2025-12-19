from sentence_transformers import SentenceTransformer, util
import numpy as np

class AnswerEvaluator:
    def __init__(self):
        # Load a lightweight model for semantic similarity
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def evaluate_answer(self, question, keyword, user_answer):
        """
        Evaluates the user's answer against a generated 'ideal' context 
        derived from the keyword and question.
        Returns a score (0-10) and feedback.
        """
        if not user_answer or len(user_answer.strip()) < 5:
            return {
                "score": 0,
                "feedback": "Answer is too short or empty."
            }

        # Construct a synthetic ideal answer for comparison
        # Since we don't have a generative LLM, we use the keyword context as the anchor
        # A good answer should be semantically close to the context of the keyword being discussed in a positive/technical light.
        ideal_anchor = f"{keyword} is a key technology/concept. It involves {keyword} features and implementation details."
        
        # We also compare against the question itself to ensure relevance
        # Embedding
        embeddings = self.model.encode([user_answer, ideal_anchor, question])
        
        # Similarity with ideal anchor
        sim_ideal = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
        
        # Similarity with question (should be somewhat related, but not too high, we want an *answer* not a repeat)
        # Actually, let's focus on the keyword relevance.
        
        # Heuristic scoring
        # 1. Keyword overlap (simple check)
        keyword_present = keyword.lower() in user_answer.lower()
        
        # 2. Semantic Score (0.0 to 1.0) -> Scale to 10
        # Enhancing the anchor to be more robust
        similarity_score = max(0, sim_ideal) * 10 
        
        # Boost score if keyword is explicitly mentioned
        if keyword_present:
            similarity_score += 2
        
        # Clamping
        final_score = min(10, max(0, int(similarity_score)))
        
        # Feedback generation
        if final_score >= 8:
            feedback = "Excellent! Your answer is relevant and covers the key concepts."
        elif final_score >= 5:
            feedback = "Good. You touched on the topic, but more detail would improve the answer."
        else:
            feedback = "Needs Improvement. The answer seems vague or off-topic."

        return {
            "score": final_score,
            "feedback": feedback
        }

if __name__ == "__main__":
    evaluator = AnswerEvaluator()
    print(evaluator.evaluate_answer("Explain Python", "Python", "Python is a high-level programming language."))
