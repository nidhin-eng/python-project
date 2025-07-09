import tkinter as tk
from tkinter import ttk, messagebox

communication_var = None
teamwork_var = None
leadership_var = None
result_label = None
skills_entry = None
education_var = None
output_text = None
feedback_entry = None

def analyze_behavioral_traits():
    communication_skills = communication_var.get()
    teamwork = teamwork_var.get()
    leadership = leadership_var.get()
    result_label.config(text=f"Behavioral Analysis Result:\n\nCommunication Skills: {communication_skills}\nTeamwork: {teamwork}\nLeadership: {leadership}")

def open_behavioral_analysis_window():
    global communication_var, teamwork_var, leadership_var, result_label

    root1 = tk.Tk()
    root1.title("Behavioral Analysis for Placement")

    communication_var = tk.IntVar()
    teamwork_var = tk.IntVar()
    leadership_var = tk.IntVar()

    communication_label = ttk.Label(root1, text="Communication Skills:")
    communication_scale = ttk.Scale(root1, from_=1, to=5, orient=tk.HORIZONTAL, variable=communication_var)

    teamwork_label = ttk.Label(root1, text="Teamwork:")
    teamwork_scale = ttk.Scale(root1, from_=1, to=5, orient=tk.HORIZONTAL, variable=teamwork_var)

    leadership_label = ttk.Label(root1, text="Leadership:")
    leadership_scale = ttk.Scale(root1, from_=1, to=5, orient=tk.HORIZONTAL, variable=leadership_var)

    def analyze_behavioral_command():
        analyze_behavioral_traits()

    analyze_button = ttk.Button(root1, text="Analyze", command=analyze_behavioral_command)
    result_label = ttk.Label(root1, text="Behavioral Analysis Result will be displayed here.")

    communication_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    communication_scale.grid(row=0, column=1, padx=10, pady=10)

    teamwork_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    teamwork_scale.grid(row=1, column=1, padx=10, pady=10)

    leadership_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    leadership_scale.grid(row=2, column=1, padx=10, pady=10)

    analyze_button.grid(row=3, column=0, columnspan=2, pady=10)
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def close_behavioral_window():
        root1.destroy()  # Close the behavioral analysis window
        open_recommendation_window()

    root1.protocol("WM_DELETE_WINDOW", close_behavioral_window)
    root1.config(bg='black')
    root1.mainloop()

def recommend_jobs():
    global education_var, skills_entry, output_text

    candidate_education = education_var.get()
    candidate_skills = skills_entry.get().lower().split(",")

    job_requirements = {
        "Software Engineer": {
            "education": "Bachelor's Degree",
            "skills": ["python","javascript","database management","c","c++","java","oracle"]
        },
        "Data Analyst": {
            "education": "Bachelor's Degree",
            "skills": ["SQL","Data Visualization","Statistics","python","java"]
        },
        "Marketing Manager": {
            "education": "Master's Degree",
            "skills": ["Marketing Strategy","Social Media Management","Analytics"]
        },
        "Full stack software developer":{
            "education":"High School Diploma",
            "skills":["python","Java","c","c++","oracle"]
        },
        "Developer":{
            "education":"Btech",
            "skills":["python","c++","c","javascript","java","machine learning","SQL","Communication skills","Cyber security"]
        },
        # Add other job requirements here...
    }

    matched_jobs = []
    for job, requirements in job_requirements.items():
        if candidate_education == requirements["education"]:
            matched_skills = set(candidate_skills) & set(requirements["skills"])
            if len(matched_skills) > 0:
                matched_jobs.append((job, matched_skills))

    if matched_jobs:
        output_text.set(f"Matched Skills: {','.join(matched_jobs[0][1])}\nRecommended Job: {matched_jobs[0][0]}")
    else:
        output_text.set("No matching jobs found")

def open_recommendation_window():
    global education_var, skills_entry, output_text

    root2 = tk.Tk()
    root2.title("Job Recommendation System")

    education_options = ["None", "High School Diploma", "Bachelor's Degree", "Master's Degree", "PhD"]
    education_var = tk.StringVar(root2)
    education_var.set(education_options[0])
    education_label = ttk.Label(root2, text="Education:")
    education_label.pack()
    education_dropdown = ttk.OptionMenu(root2, education_var, *education_options)
    education_dropdown.pack()

    skills_label = ttk.Label(root2, text="Skills (comma-separated):")
    skills_label.pack()
    skills_entry = ttk.Entry(root2)
    skills_entry.pack()

    output_text = tk.StringVar()
    output_label = ttk.Label(root2, textvariable=output_text)
    output_label.pack()

    recommend_button = ttk.Button(root2, text="Recommend Jobs", command=recommend_jobs)
    recommend_button.pack()

    def close_recommendation_window():
        root2.destroy()  # Close the recommendation window
        open_feedback_window()

    root2.protocol("WM_DELETE_WINDOW", close_recommendation_window)
    root2.config(bg='black')
    root2.mainloop()

def submit_feedback():
    global feedback_entry

    feedback = feedback_entry.get("1.0", "end-1c")
    messagebox.showinfo("Feedback Submitted", f"Thank you for your feedback:\n\n{feedback}")

def open_feedback_window():
    global feedback_entry

    root3 = tk.Tk()
    root3.title("Feedback Submission")

    feedback_label = tk.Label(root3, text="Your Feedback:")
    feedback_label.pack()

    feedback_entry = tk.Text(root3, height=5, width=30)
    feedback_entry.pack()

    submit_button = tk.Button(root3, text="Submit Feedback", command=submit_feedback)
    submit_button.pack()
    root3.config(bg='black')
    root3.mainloop()

open_behavioral_analysis_window()
