class EDAEngine:
    def __init__(self, exploratory_analysis, students_above_70, student_form):
        self.exploratory_analysis = exploratory_analysis
        self.students_above_70    = students_above_70
        self.student_form         = student_form
    
    def perform_eda(self):
        self.student_data      = self.student_form.get_all_student_data()
        highest_student        = self.get_highest_student()
        sorted_scores          = self.sort_student_data()
        eda                    = self.prepare_eda(highest_student, sorted_scores)
        students_above_70_list = self.prepare_list()
        
        # display EDA on the eda section
        self.exploratory_analysis.config( text=eda )

        # display list of students above 70
        self.display_list(students_above_70_list)
    
    def display_list(self, s_above_70):
        students_above_70 = self.students_above_70
        
        students_above_70.delete("0", "end")
        students_above_70.insert("end", "Students above 70:")
        students_above_70.insert("end", "")
        for s in s_above_70:
            self.students_above_70.insert("end", f'{s[2]} - {s[1]} - {s[0]}')
    
    def get_highest_student(self):
        highest_student = ['', '', -1]
        for student in self.student_form.get_all_student_data():
            if int(highest_student[2]) < int(student[2]):
                highest_student = student
        return highest_student
    
    def prepare_eda(self, highest_student, sorted_scores):
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
    
    def sort_student_data(self):
        sorted_scores = [ int(row[2]) for row in self.student_data ]
        sorted_scores.sort(reverse=True)
        return sorted_scores

    def prepare_list(self):
        student_data = self.student_data
        student_list = [ student for student in student_data if int(student[2]) >= 70 ]
        student_list.sort(key=lambda student : student[2], reverse=True)
        return student_list
