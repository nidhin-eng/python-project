import tkinter as tk
from tkinter import ttk, messagebox

class PerformanceAnalytics:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Placement Recommendation Performance Analytics")
        self.root.config(bg='black')
        self.gpa_var = tk.StringVar()
        self.coding_skills_var = tk.StringVar()
        self.communication_skills_var = tk.StringVar()

        gpa_label = ttk.Label(self.root, text="GPA:")
        gpa_entry = ttk.Entry(self.root, textvariable=self.gpa_var)

        coding_skills_label = ttk.Label(self.root, text="Coding Skills:")
        coding_skills_entry = ttk.Entry(self.root, textvariable=self.coding_skills_var)

        communication_skills_label = ttk.Label(self.root, text="Communication Skills:")
        communication_skills_entry = ttk.Entry(self.root, textvariable=self.communication_skills_var)

        analyze_button = ttk.Button(self.root, text="Analyze", command=self.analyze_performance)

        self.result_text = tk.StringVar()
        result_label = ttk.Label(self.root, textvariable=self.result_text)

        gpa_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        gpa_entry.grid(row=0, column=1, padx=10, pady=10)

        coding_skills_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        coding_skills_entry.grid(row=1, column=1, padx=10, pady=10)

        communication_skills_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        communication_skills_entry.grid(row=2, column=1, padx=10, pady=10)

        analyze_button.grid(row=3, column=0, columnspan=2, pady=10)
        result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def analyze_performance(self):
        try:
            gpa = float(self.gpa_var.get())
            coding_skills = int(self.coding_skills_var.get())
            communication_skills = int(self.communication_skills_var.get())

            result = (f"Performance Analytics Result:\n\n"
                      f"Average GPA: {gpa:.2f}\n"
                      f"Coding Skills: {coding_skills}\n"
                      f"Communication Skills: {communication_skills}")
            self.result_text.set(result)
        except ValueError:
            self.result_text.set("Invalid input. Please enter valid numeric values.")
        self.root.config(bg='black')
        self.root.mainloop()

class ExperienceAssessment:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Experience Assessment")

        self.questions = [
            "How many years of programming experience do you have?",
            "Have you worked on any large-scale projects? (Yes/No)",
            "Do you have experience with version control systems? (Yes/No)",
            "Have you used any testing frameworks in your projects? (Yes/No)"
            # Add more questions as needed
        ]

        self.answers = []
        self.current_question_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to Experience Assessment!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.question_label = tk.Label(self.root, text=self.questions[self.current_question_index])
        self.question_label.pack(pady=5)

        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack(pady=5)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)
        self.root.config(bg='black')
        self.root.mainloop()

    def next_question(self):
        answer = self.answer_entry.get()

        if not answer:
            messagebox.showwarning("Warning", "Please provide an answer.")
            return

        self.answers.append(answer)
        self.answer_entry.delete(0, tk.END)
        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question_index])
        else:
            self.evaluate_experience()

    def evaluate_experience(self):
        experience_score = sum(1 for answer in self.answers if answer.lower() == 'yes')
        messagebox.showinfo("Assessment Result", f"Your experience score is {experience_score}.")
        self.root.destroy()

class ContinuousLearningApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Continuous Learning Tracker")
        self.root.config(bg='black')
        self.skill_var = tk.StringVar()
        self.hours_var = tk.DoubleVar()

        tk.Label(self.root, text="Skill:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.skill_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Hours Spent:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.hours_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Add Entry", command=self.add_entry).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="View Progress", command=self.view_progress).grid(row=3, column=0, columnspan=2, pady=10)
        
        self.learning_data = []

    def add_entry(self):
        skill = self.skill_var.get()
        hours = self.hours_var.get()

        if skill and hours > 0:
            self.learning_data.append((skill, hours))
            messagebox.showinfo("Success", f"Entry added: Skill - {skill}, Hours - {hours}")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please enter valid skill and hours.")

    def view_progress(self):
        if not self.learning_data:
            messagebox.showinfo("No Data", "No learning data available.")
        else:
            progress_message = "Learning Progress:\n"
            for entry in self.learning_data:
                progress_message += f"{entry[0]} - {entry[1]} hours\n"

            messagebox.showinfo("Learning Progress", progress_message)

    def clear_entries(self):
        self.skill_var.set("")
        self.hours_var.set(0.0)
        self.root.config(bg='black')
        self.root.mainloop()

if __name__ == "__main__":
    # Create instances of each class in separate windows
    PerformanceAnalytics()
    ExperienceAssessment()
    ContinuousLearningApp()

