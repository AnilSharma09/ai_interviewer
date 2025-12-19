import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

# Suppress warnings for simple NLP tasks
warnings.filterwarnings("ignore")

class AnswerEvaluator:
    def __init__(self):
        # Load spaCy model strictly matching requirements
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            raise RuntimeError("Model 'en_core_web_sm' is missing. Ensure it is installed via requirements.txt.")

    def evaluate_answer(self, user_answer, keywords):
        """
        Evaluates the user's answer based on keyword coverage and semantic similarity.
        Returns a score (0-100) and feedback text.
        """
        if not user_answer or not user_answer.strip():
            return 0, "No answer provided.", []

        # 1. NLP Processing - Lemmatization
        doc_answer = self.nlp(user_answer.lower())
        lemmatized_answer_tokens = {token.lemma_ for token in doc_answer if not token.is_stop and not token.is_punct}
        
        # 2. Keyword Matching (Score Component 1)
        # Convert keywords to lemmas to match variations (e.g., "modification" -> "modify")
        lemmatized_keywords = set()
        for kw in keywords:
            kw_doc = self.nlp(kw.lower())
            for token in kw_doc:
                lemmatized_keywords.add(token.lemma_)
        
        matched_keywords = lemmatized_keywords.intersection(lemmatized_answer_tokens)
        match_count = len(matched_keywords)
        total_keywords = len(lemmatized_keywords)
        
        keyword_score = (match_count / total_keywords) * 100 if total_keywords > 0 else 0
        
        # 3. Use spaCy similarity (Score Component 2)
        # Create a document from keywords to compare against answer
        doc_keywords = self.nlp(" ".join(keywords))
        
        # Note: en_core_web_sm doesn't have static vectors, so this uses context tensors.
        # It's good enough for basic context estimation.
        similarity_score = doc_answer.similarity(doc_keywords) * 100
        
        # 4. Final Weighted Score
        # Give more weight to explicit keyword matches
        final_score = (0.7 * keyword_score) + (0.3 * similarity_score)
        final_score = min(100, max(0, final_score)) # Clamp
        
        # Generate Feedback
        missing_keywords = list(lemmatized_keywords - matched_keywords)
        
        feedback = f"Relevance Score: {final_score:.1f}/100."
        if final_score > 80:
            feedback += " Excellent answer! You covered the key concepts."
        elif final_score > 50:
            feedback += " Good attempt. Try to include more specific terminology."
        else:
            feedback += " Your answer seems a bit off or too brief."

        return final_score, feedback, missing_keywords
