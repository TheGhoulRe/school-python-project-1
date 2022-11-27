import csv
import os

def get_all_student_data():
    file       = open("students.csv", "r")
    csv_reader = csv.reader(file)
    data       = []

    # ignore header
    next( csv_reader )

    for row in csv_reader: data.append(row)
    file.close()
    return data

def create_add_student(name_widget, mat_no_widget, score_widget):
    filepath = "students.csv"

    if not os.path.exists(filepath):
        setup_filepath()
    
    def add_student():
        name   = name_widget.get("1.0", "end-1c")
        mat_no = mat_no_widget.get("1.0", "end-1c")
        score  = score_widget.get("1.0", "end-1c")
        line   = f'{name},{mat_no},{score}\n'
        file   = open(filepath, "a")
        file.write(line)
        file.close()

        # clear input boxes
        name_widget.delete("1.0", "end-1c")
        mat_no_widget.delete("1.0", "end-1c")
        score_widget.delete("1.0", "end-1c")
    
    return add_student


def setup_filepath():
        file = open("students.csv", "w")
        file.write("Full name,Matric No.,Score\n")
        file.close()