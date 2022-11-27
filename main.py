from tkinter import Tk, Label, Text, Button, Listbox
from student_form import create_add_student
from eda_engine import create_eda_engine

def main(root):
    root.geometry("500x500")
    root.title("Project 1")
    setup_ui(root)
    root.mainloop()

def setup_ui(root):
    (name, mat_no, score) = setup_text_fields( root )
    exploratory_analysis  = setup_exploratory_analysis_output( root )
    s_above_70_widget     = setup_students_above_70_output( root )
    add_student           = create_add_student(name, mat_no, score)
    eda_engine            = create_eda_engine(exploratory_analysis, s_above_70_widget)

    setup_save_student_button(root, add_student)
    setup_perform_eda_button( root, eda_engine )
    setup_text_labels( root )

def setup_text_fields(root):
    name = Text(root)
    name.place(x=197, y=32, width=271, height=25)
    mat_no = Text(root)
    mat_no.place(x=197, y=67, width=271, height=25)
    score = Text(root)
    score.place(x=197, y=102, width=271, height=25)

    return (name, mat_no, score)

def setup_exploratory_analysis_output(root):
    exploratory_analysis = Label(root, font=("regular", 9), justify="left")
    exploratory_analysis.place(x=32, y=198, width=156, height=270)
    return exploratory_analysis

def setup_students_above_70_output(root):
    students_above_70 = Listbox(root, font=("regular", 10))
    students_above_70.place(x=206, y=198, width=262, height=270)
    return students_above_70

def setup_save_student_button(root, add_student):
    Button(
        root,
        text="save student score",
        font=("regular", 13),
        command=add_student,
    ).place(x=32, y=137, width=177, height=39)

def setup_perform_eda_button(root, eda_engine):
    Button(
        root,
        text="EDA for saved students",
        font=("regular", 10),
        command=eda_engine
    ).place(x=291, y=137, width=177, height=39)

def setup_text_labels(root):
    Label(root, text="Full Name", font=("regular", 13)).place(x=32, y=32)
    Label(root, text="Matric No", font=("regular", 13)).place(x=32, y=67)
    Label(root, text="Score", font=("regular", 13)).place(x=32, y=102)


if __name__ == "__main__":
    main( Tk() )