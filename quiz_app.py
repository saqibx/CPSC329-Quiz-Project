

import tkinter as tk
from tkinter import font
import random
from quiz_data import get_questions
from ui_components import create_ui_components




class CybersecurityQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity Quiz")
        self.root.geometry("800x500")
        self.root.configure(bg="#2c3e50")


        self.title_font = font.Font(family="Arial", size=24, weight="bold")
        self.question_font = font.Font(family="Arial", size=14)
        self.button_font = font.Font(family="Arial", size=12, weight="bold")
        self.score_font = font.Font(family="Arial", size=18, weight="bold")


        self.questions = get_questions()
        self.current_question = 0
        self.score = 0
        self.total_questions = len(self.questions)


        random.shuffle(self.questions)


        self.welcome_frame, self.quiz_frame, self.results_frame, self.ui_elements = create_ui_components(
            self.root,
            self.title_font,
            self.question_font,
            self.button_font,
            self.score_font,
            self.start_quiz,
            self.check_answer,
            self.restart_quiz
        )



        self.progress_label = self.ui_elements["progress_label"]
        self.question_label = self.ui_elements["question_label"]
        self.score_label = self.ui_elements["score_label"]
        self.feedback_label = self.ui_elements["feedback_label"]


        self.welcome_frame.pack(pady=50, fill=tk.BOTH, expand=True)

    def start_quiz(self):

        self.welcome_frame.pack_forget()
        self.quiz_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        self.display_question()

    def display_question(self):

        self.progress_label.config(text=f"Question {self.current_question + 1} of {self.total_questions}")


        self.question_label.config(text=self.questions[self.current_question]["question"])

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.current_question]["answer"]

        if user_answer == correct_answer:
            self.score += 1

        self.current_question += 1


        if self.current_question < self.total_questions:
            self.display_question()
        else:
            self.show_results()

    def show_results(self):

        self.quiz_frame.pack_forget()
        self.results_frame.pack(pady=50, fill=tk.BOTH, expand=True)


        percentage = (self.score / self.total_questions) * 100


        self.score_label.config(text=f"Your Score: {self.score}/{self.total_questions} ({percentage:.1f}%)")


        if percentage >= 90:
            feedback = "Excellent! You're a cybersecurity expert!"
        elif percentage >= 70:
            feedback = "Great job! You have solid cybersecurity knowledge."
        elif percentage >= 50:
            feedback = "Good effort! Keep learning about cybersecurity."
        else:
            feedback = "You might want to study more about cybersecurity basics."

        self.feedback_label.config(text=feedback)

    def restart_quiz(self):
        self.current_question = 0
        self.score = 0


        random.shuffle(self.questions)


        self.results_frame.pack_forget()
        self.welcome_frame.pack(pady=50, fill=tk.BOTH, expand=True)