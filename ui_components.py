
import tkinter as tk


def create_ui_components(root, title_font, question_font, button_font, score_font,
                         start_callback, check_answer_callback, restart_callback):


    welcome_frame = tk.Frame(root, bg="#2c3e50")

    # All of this is just related to creating the labels and making them look good
    tk.Label(
        welcome_frame,
        text="Cybersecurity Quiz",
        font=title_font,
        bg="#2c3e50",
        fg="#ecf0f1"
    ).pack(pady=30)

    tk.Label(
        welcome_frame,
        text="Test your knowledge with true/false questions about cybersecurity.",
        font=question_font,
        bg="#2c3e50",
        fg="#ecf0f1",
        wraplength=600
    ).pack(pady=20)

    start_button = tk.Button(
        welcome_frame,
        text="Start Quiz",
        command=start_callback,
        font=button_font,
        bg="#3498db",
        fg="white",
        padx=20,
        pady=10,
        relief=tk.FLAT,
        activebackground="#2980b9"
    )
    start_button.pack(pady=40)





    # creating quiz main frame
    quiz_frame = tk.Frame(root, bg="#2c3e50")


    progress_label = tk.Label(
        quiz_frame,
        text="",
        font=question_font,
        bg="#2c3e50",
        fg="#ecf0f1"
    )
    progress_label.pack(pady=10)


    question_container = tk.Frame(quiz_frame, bg="#34495e", padx=30, pady=30)
    question_container.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)

    question_label = tk.Label(
        question_container,
        text="",
        font=question_font,
        bg="#34495e",
        fg="white",
        wraplength=600,
        justify=tk.CENTER
    )
    question_label.pack(pady=30)


    button_frame = tk.Frame(question_container, bg="#34495e")
    button_frame.pack(pady=20)


    true_button = tk.Button(
        button_frame,
        text="True",
        command=lambda: check_answer_callback(True),
        font=button_font,
        bg="#2ecc71",
        fg="white",
        width=10,
        padx=20,
        pady=10,
        relief=tk.FLAT,
        activebackground="#27ae60"
    )
    true_button.pack(side=tk.LEFT, padx=10)


    false_button = tk.Button(
        button_frame,
        text="False",
        command=lambda: check_answer_callback(False),
        font=button_font,
        bg="#e74c3c",
        fg="white",
        width=10,
        padx=20,
        pady=10,
        relief=tk.FLAT,
        activebackground="#c0392b"
    )
    false_button.pack(side=tk.LEFT, padx=10)


    results_frame = tk.Frame(root, bg="#2c3e50")

    result_title = tk.Label(
        results_frame,
        text="Quiz Complete!",
        font=title_font,
        bg="#2c3e50",
        fg="#ecf0f1"
    )
    result_title.pack(pady=30)

    score_label = tk.Label(
        results_frame,
        text="",
        font=score_font,
        bg="#2c3e50",
        fg="#ecf0f1"
    )
    score_label.pack(pady=20)

    feedback_label = tk.Label(
        results_frame,
        text="",
        font=question_font,
        bg="#2c3e50",
        fg="#ecf0f1"
    )
    feedback_label.pack(pady=10)


    final_button_frame = tk.Frame(results_frame, bg="#2c3e50")
    final_button_frame.pack(pady=40)

    restart_button = tk.Button(
        final_button_frame,
        text="Try Again",
        command=restart_callback,
        font=button_font,
        bg="#3498db",
        fg="white",
        padx=15,
        pady=8,
        relief=tk.FLAT,
        activebackground="#2980b9"
    )
    restart_button.pack(side=tk.LEFT, padx=10)

    exit_button = tk.Button(
        final_button_frame,
        text="Exit",
        command=root.destroy,
        font=button_font,
        bg="#95a5a6",
        fg="white",
        padx=15,
        pady=8,
        relief=tk.FLAT,
        activebackground="#7f8c8d"
    )
    exit_button.pack(side=tk.LEFT, padx=10)


    ui_elements = {
        "progress_label": progress_label,
        "question_label": question_label,
        "true_button": true_button,
        "false_button": false_button,
        "score_label": score_label,
        "feedback_label": feedback_label,
        "restart_button": restart_button,
        "exit_button": exit_button
    }

    return welcome_frame, quiz_frame, results_frame, ui_elements