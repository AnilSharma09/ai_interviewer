import spacy
import random

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

class QuestionGenerator:
    def __init__(self):
        self.templates = [
            "Can you explain the concept of {keyword} and how it is used in a professional setting?",
            "What are the key advantages of using {keyword} compared to its alternatives?",
            "Describe a challenging situation where you had to apply your knowledge of {keyword}.",
            "How would you optimize a system that relies heavily on {keyword}?",
            "What common pitfalls should developers avoid when working with {keyword}?"
        ]

    def extract_keywords(self, text):
        """Extracts relevant keywords (NOUN, PROPN) from the job description."""
        doc = nlp(text)
        keywords = set()
        for token in doc:
            if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop and token.is_alpha:
                keywords.add(token.text)
        
        # Sort by frequency/relevance could be added here, currently just taking unique set
        return list(keywords)

    def generate_questions(self, job_description, num_questions=5):
        """Generates a list of questions based on extracted keywords."""
        if not job_description:
            return []

        keywords = self.extract_keywords(job_description)
        
        if len(keywords) < num_questions:
            # Fallback if few keywords found
            selected_keywords = keywords * (num_questions // len(keywords) + 1)
        else:
            selected_keywords = keywords

        questions = []
        # Shuffle to get random mix
        random.shuffle(selected_keywords)

        for i in range(num_questions):
            keyword = selected_keywords[i]
            template = random.choice(self.templates)
            question_text = template.format(keyword=keyword)
            questions.append({
                "question": question_text,
                "keyword": keyword
            })
        
        return questions

if __name__ == "__main__":
    # Test
    gen = QuestionGenerator()
    jd = "We are looking for a Python Developer with experience in Django, SQL, and AWS."
    print(gen.generate_questions(jd))
