from student_form import get_all_student_data

def create_eda_engine(exploratory_analysis, s_above_70_widget):
    def perform_eda():
        student_data           = get_all_student_data()
        highest_student        = get_highest_student(student_data)
        sorted_scores          = sort_student_data(student_data)
        eda                    = prepare_eda(highest_student, sorted_scores)
        students_above_70_list = prepare_list(student_data)
        
        # display EDA on the eda section
        exploratory_analysis.config( text=eda )

        # display list of students above 70
        display_list(s_above_70_widget, students_above_70_list)
    
    return perform_eda

def get_highest_student(student_data):
    highest_student = ['', '', -1]
    for student in student_data:
        if int(highest_student[2]) < int(student[2]):
            highest_student = student
    return highest_student

def sort_student_data(student_data):
    sorted_scores = [ int(row[2]) for row in student_data ]
    sorted_scores.sort(reverse=True)
    return sorted_scores

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

def prepare_list(student_data):
    student_list = [ student for student in student_data if int(student[2]) >= 70 ]
    student_list.sort(key=lambda student : student[2], reverse=True)
    return student_list

def display_list(s_above_70_widget, s_above_70):
    s_above_70_widget.delete("0", "end")
    s_above_70_widget.insert("end", "Students above 70:")
    s_above_70_widget.insert("end", "")
    for s in s_above_70:
        s_above_70_widget.insert("end", f'{s[2]} - {s[1]} - {s[0]}')