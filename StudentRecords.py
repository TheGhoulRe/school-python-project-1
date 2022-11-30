from tkinter import Tk, Label, Text, Button, Listbox
import os
import csv

class StudentRecords:
    def __init__(self, root):
        self.root = root
        self.student_data = []
        self.setup_filepath()
        self.setup_window()
        self.setup_ui()            
        root.mainloop()

    def setup_filepath(self):
        self.filepath = "students.csv"
        if not os.path.exists(self.filepath):
            self.write_file()
            file = open(self.filepath, "w")
            file.write("Full name,Matric No.,Score\n")
            file.close()
    
    def setup_window(self):
        root = self.root
        root.geometry("500x500")
        root.title("Student Records")
    
    def setup_ui(self):
        self.setup_text_labels()
        self.setup_text_fields()
        self.setup_exploratory_analysis_output()
        self.setup_students_above_70_output()
        self.setup_save_student_button()
        self.setup_perform_eda_button()
    
    def setup_text_labels(self):
        Label(self.root, text="Full Name", font=("regular", 13)).place(x=32, y=32)
        Label(self.root, text="Matric No", font=("regular", 13)).place(x=32, y=67)
        Label(self.root, text="Score", font=("regular", 13)).place(x=32, y=102)

    def setup_text_fields(self):
        root = self.root
        self.name = Text(root)
        self.mat_no = Text(root)
        self.score = Text(root)
        self.name.place(x=197, y=32, width=271, height=25)
        self.mat_no.place(x=197, y=67, width=271, height=25)
        self.score.place(x=197, y=102, width=271, height=25)

    def setup_exploratory_analysis_output(self):
        self.exploratory_analysis = Label(self.root, font=("regular", 9), justify="left")
        self.exploratory_analysis.place(x=32, y=198, width=156, height=270)

    def setup_students_above_70_output(self):
        self.students_above_70 = Listbox(self.root, font=("regular", 10))
        self.students_above_70.place(x=206, y=198, width=262, height=270)

    def setup_save_student_button(self):
        Button(
            self.root,
            text="save student score",
            font=("regular", 13),
            command=self.add_student,
        ).place(x=32, y=137, width=177, height=39)

    def setup_perform_eda_button(self):
        Button(
            self.root,
            text="EDA for saved students",
            font=("regular", 10),
            command=self.calculate_eda
        ).place(x=291, y=137, width=177, height=39)
    
    def add_student(self):
        name   = self.name.get("1.0", "end-1c")
        mat_no = self.mat_no.get("1.0", "end-1c")
        score  = self.score.get("1.0", "end-1c")
        line   = f'{name},{mat_no},{score}\n'
        
        file   = open(self.filepath, "a")
        file.write(line)
        file.close()

        self.name.delete("1.0", "end-1c")
        self.mat_no.delete("1.0", "end-1c")
        self.score.delete("1.0", "end-1c")
    
    def calculate_eda(self):
        self.read_student_data()
        highest_student = self.get_highest_student()
        sorted_scores = self.sort_student_data()
        eda = StudentRecords.prepare_eda(highest_student, sorted_scores)
        students_above_70_list = self.prepare_list()
        self.exploratory_analysis.config( text=eda )
        self.display_list(students_above_70_list)
    
    def read_student_data(self):
        file = open(self.filepath, "r")

        csv_reader = csv.reader(file)
        next( csv_reader )
        for row in csv_reader:
            self.student_data.append(row)

        file.close()
    
    def get_highest_student(self):
        highest_student = ['', '', -1]
        for student in self.student_data:
            if int(highest_student[2]) < int(student[2]):
                highest_student = student
        return highest_student

    def sort_student_data(self):
        sorted_scores = [ int(row[2]) for row in self.student_data ]
        sorted_scores.sort(reverse=True)
        return sorted_scores

    def prepare_list(self):
        student_list = [ student for student in self.student_data if int(student[2]) >= 70 ]
        student_list.sort(key=lambda student : student[2], reverse=True)
        return student_list

    def display_list(self, s_above_70):
        self.students_above_70.delete("0", "end")
        self.students_above_70.insert("end", "Students above 70:")
        self.students_above_70.insert("end", "")
        for s in s_above_70:
            self.students_above_70.insert("end", f'{s[2]} - {s[1]} - {s[0]}')
    
    @staticmethod
    def prepare_eda(highest_student, sorted_scores):
        max_num = max(sorted_scores)
        min_num = min(sorted_scores)
        median = sorted_scores[len(sorted_scores) // 2]
        mean = sum(sorted_scores) // len(sorted_scores)

        text = f"Exploratory data analysis:\n\n"\
            f"Mean: {mean}\n\n"\
            f"Median: {median}\n\n"\
            f"Maximum score: {max_num}\n\n"\
            f"Minimum score: {min_num}\n\n"\
            f"Best student:\n"\
            f"  {highest_student[0]}\n"\
            f"  {highest_student[1]}\n"\
            f"  {highest_student[2]}"
        return text

if __name__ == "__main__":
    StudentRecords( Tk() )