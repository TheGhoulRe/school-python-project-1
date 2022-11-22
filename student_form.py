import csv
import os

class StudentForm:
    def __init__(self, filepath, name, mat_no, score):
        self.name = name
        self.mat_no = mat_no
        self.score = score
        self.filepath = filepath
        self.setup_filepath()
    
    def setup_filepath(self):
        filepath = self.filepath

        # if file doesn't exist, create a new one
        if not os.path.exists(filepath):
            file = open(filepath, "w")
            file.write("Full name,Matric No.,Score\n")
            file.close()
    
    def add_student(self):
        name   = self.name.get("1.0", "end-1c")
        mat_no = self.mat_no.get("1.0", "end-1c")
        score  = self.score.get("1.0", "end-1c")
        line   = f'{name},{mat_no},{score}\n'
        file   = open(self.filepath, "a")
        file.write(line)
        file.close()

        # clear input boxes
        self.name.delete("1.0", "end-1c")
        self.mat_no.delete("1.0", "end-1c")
        self.score.delete("1.0", "end-1c")
    
    def get_all_student_data(self):
        file       = open(self.filepath, "r")
        csv_reader = csv.reader(file)
        data       = []

        # ignore header
        next( csv_reader )

        for row in csv_reader: data.append(row)
        file.close()
        return data

        