

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import PyPDF2

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Application")

        self.frames = [self.create_education_window, self.create_job_assessment_window, self.create_resume_window]
        self.current_frame = 0
        self.create_next_frame()

    def create_next_frame(self):
        if self.current_frame < len(self.frames):
            self.clear_window()
            self.frames[self.current_frame]()
            self.current_frame += 1
        else:
            self.root.destroy()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_education_window(self):
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.ethnicity_var = tk.StringVar()
        self.gender_var = tk.StringVar()

        name_label = tk.Label(self.root, text="Name:")
        name_label.pack()
        name_entry = ttk.Entry(self.root, textvariable=self.name_var)
        name_entry.pack()

        age_label = tk.Label(self.root, text="Age:")
        age_label.pack()
        age_entry = ttk.Entry(self.root, textvariable=self.age_var)
        age_entry.pack()

        ethnicity_options = ["Asian", "European", "Hispanic", "African"]
        ethnicity_label = tk.Label(self.root, text="Ethnicity:")
        ethnicity_label.pack()
        ethnicity_menu = ttk.Combobox(self.root, textvariable=self.ethnicity_var, values=ethnicity_options)
        ethnicity_menu.pack()

        gender_options = ["Male", "Female", "Other"]
        gender_label = tk.Label(self.root, text="Gender:")
        gender_label.pack()
        gender_menu = ttk.Combobox(self.root, textvariable=self.gender_var, values=gender_options)
        gender_menu.pack()

        submit_button = ttk.Button(self.root, text="Submit", command=self.create_next_frame)
       
        submit_button.pack()

    def create_job_assessment_window(self):
        self.answers = [tk.StringVar() for _ in range(5)]

        questions = [
            "Do you have experience in programming? (Y/N)",
            "Rate your proficiency in a programming language (1-10):",
            "Have you worked on any software projects? (Y/N)",
            "How do you handle complex problem-solving?",
            "How well do you work in a team? (1-10)",
        ]

        for i, question in enumerate(questions):
            tk.Label(self.root, text=question).pack()
            if "proficiency" in question.lower():
                tk.Scale(self.root, from_=1, to=10, orient=tk.HORIZONTAL, variable=self.answers[i]).pack()
            else:
                tk.Entry(self.root, textvariable=self.answers[i]).pack()

        submit_button = ttk.Button(self.root, text="Submit", command=self.create_next_frame)
        submit_button.pack()

    def create_resume_window(self):
        degree_label = tk.Label(self.root, text="Degree:")
        degree_label.pack()
        degree_entry = tk.Entry(self.root)
        degree_entry.pack()

        major_label = tk.Label(self.root, text="Major:")
        major_label.pack()
        major_entry = tk.Entry(self.root)
        major_entry.pack()

        school_label = tk.Label(self.root, text="College:")
        school_label.pack()
        school_entry = tk.Entry(self.root)
        school_entry.pack()

        grad_year_label = tk.Label(self.root, text="Graduation Year:")
        grad_year_label.pack()
        grad_year_entry = tk.Entry(self.root)
        grad_year_entry.pack()

        education_label = tk.Label(self.root, text="")
        education_label.pack()

        def display_education():
            education_info = f"Education Background:\n\n" \
                             f"Degree: {degree_entry.get()}\n" \
                             f"Major: {major_entry.get()}\n" \
                             f"College: {school_entry.get()}\n" \
                             f"Graduation Year: {grad_year_entry.get()}"
            education_label.config(text=education_info)

        submit_button = tk.Button(self.root, text="Submit",bg='white',fg='violet', command=display_education)
        submit_button.pack()

        def extract_resume_content(file_path):
            content = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    content += page.extract_text()
            return content

        def open_file_dialog():
            resume_path = filedialog.askopenfilename()
            if resume_path:
                resume_content = extract_resume_content(resume_path)
                resume_display.delete("1.0", tk.END)
                resume_display.insert(tk.END, resume_content)

        resume_button = tk.Button(self.root, text="Select Resume", command=open_file_dialog)
        resume_button.pack()

        resume_display = tk.Text(self.root, height=20, width=80)
        resume_display.pack()

def main():
    root = tk.Tk()
    app = Application(root)
    root.configure(bg='black')
    root.mainloop()

if __name__ == "__main__":
    main()

