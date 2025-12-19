import spacy
import random
import spacy
import subprocess
import sys
import spacy
import os

class QuestionGenerator:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), "en_core_web_sm")
        self.nlp = spacy.load(model_path)

        # Question Bank with expected keywords for evaluation
        self.question_bank = {
            "Python": [
                {
                    "question": "What is the difference between list and tuple in Python?",
                    "keywords": ["mutable", "immutable", "change", "syntax", "brackets", "parentheses"]
                },
                {
                    "question": "Explain the concept of decorators in Python.",
                    "keywords": ["function", "modify", "wrapper", "argument", "call", "@"]
                },
                {
                    "question": "What are Python generators and how do they differ from iterators?",
                    "keywords": ["yield", "memory", "efficient", "next", "iterable"]
                },
                {
                    "question": "How memory is managed in Python?",
                    "keywords": ["heap", "private", "garbage", "collection", "reference", "counting"]
                }
            ],
            "React": [
                {
                    "question": "What are hooks in React?",
                    "keywords": ["state", "feature", "class", "functional", "component", "lifecycle"]
                },
                {
                    "question": "Explain the Virtual DOM.",
                    "keywords": ["copy", "real", "dom", "rendering", "performance", "diffing", "algorithm"]
                },
                {
                    "question": "What is the use of useEffect?",
                    "keywords": ["side", "effect", "data", "fetching", "subscription", "render"]
                }
            ],
            "Machine Learning": [
                {
                    "question": "What is the difference between supervised and unsupervised learning?",
                    "keywords": ["label", "data", "training", "outcome", "cluster", "classification"]
                },
                {
                    "question": "Explain the bias-variance tradeoff.",
                    "keywords": ["error", "model", "complexity", "overfitting", "underfitting", "prediction"]
                },
                {
                    "question": "What is a confusion matrix?",
                    "keywords": ["performance", "classification", "true", "positive", "false", "negative"]
                }
            ],
            "General Developer": [
                {
                    "question": "Explain Git and its importance.",
                    "keywords": ["version", "control", "history", "collaborate", "branch", "repository"]
                },
                {
                    "question": "What is REST API?",
                    "keywords": ["representational", "state", "transfer", "http", "method", "resource"]
                }
            ]
        }

    def generate_questions(self, role, num_questions=3):
        """
        Generates a list of questions based on the role.
        Uses NLP to standardize the role name if needed.
        """
        # Simple NLP usage to clean/standardize role input
        doc = self.nlp(role)
        # In a real app, we might extract entities, but here we just match strings safely
        clean_role = role
        
        # Soft matching for roles
        if "python" in role.lower():
            target_role = "Python"
        elif "react" in role.lower():
            target_role = "React"
        elif "machine" in role.lower() or "learning" in role.lower() or "ml" in role.lower():
            target_role = "Machine Learning"
        else:
            target_role = "General Developer"

        questions = self.question_bank.get(target_role, self.question_bank["General Developer"])
        
        # Return random selection if we have enough, else all
        return random.sample(questions, min(len(questions), num_questions))
