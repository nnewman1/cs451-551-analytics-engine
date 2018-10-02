"""
Nicholas Newman
CS551SE
09/30/2018
Class Analytics Engine 
"""
import json

class classnumba1():
    data = []
    def __init__(self):
    	"""
		Create a class called classnumba1 and importing the json file that is on my local machine.
		"""
        with open('/Users/Nick/Documents/CS551SE/CS551-AnalyticsHw6-Repo/cs451-551-analytics-engine/data/grade-data.json') as f:
            self.data = json.loads(f.read())


    def total_avg(self):
    	"""
		Create a Function called total_avg that returns the Average Final Grade for the entire dataset 
		GPA
		"""
        final_grade = 0
        total_count = 0
        for i in self.data:
            if i[3] == 'A':
                final_grade += 4.0
            elif i[3] == 'B':
                final_grade += 3.0
            elif i[3] == 'C':
                final_grade += 2.0
            elif i[3] == 'D':
                final_grade += 1.0
            elif i[3] == 'F':
                final_grade += 0.0
        total_avg = final_grade//len(self.data)

        #print total_avg
        return total_avg

    def total_mid_avg(self):
    	"""
		Create a Function called total_mid_avg that returns the Average Midterm Grade for the entire dataset 
		GPA
		"""
        mid_grade = 0
        total_count = 0
        for i in self.data:
            if i[2] == 'A':
                mid_grade += 4.0
            elif i[2] == 'B':
                mid_grade += 3.0
            elif i[2] == 'C':
                mid_grade += 2.0
            elif i[2] == 'D':
                mid_grade += 1.0
            elif i[2] == 'F':
                mid_grade += 0.0
        total_mid_avg = mid_grade//len(self.data)

        #print total_mid_avg
        return total_mid_avg

    def total_change(self):
    	"""
		Create a Function called total_change that returns the Average grade change between the midterm and the final grade for the entire dataset 
		1.0 = +1 GPA
		-1.0 = -1 GPA
		"""
        final_grade1 = self.total_avg()
        mid_grade1 = self.total_mid_avg()
        change1 = mid_grade1 - final_grade1
        #print change1
        return change1

    def total_grade_count(self):
    	"""
		Create a Function called total_grade_count that returns the count for each specific grade for the entire dataset 
		[grade_A_total,grade_B_total,grade_C_total,grade_D_total,grade_F_total]
		"""
        grade_A_total, grade_B_total, grade_C_total, grade_D_total, grade_F_total, = 0,0,0,0,0
        for i in self.data:
            if i[3] == 'A':
                grade_A_total += 1
            elif i[3] == 'B':
                grade_B_total += 1
            elif i[3] == 'C':
                grade_C_total += 1
            elif i[3] == 'D':
                grade_D_total += 1
            elif i[3] == 'F':
                grade_F_total += 1

        total = [grade_A_total,grade_B_total,grade_C_total,grade_D_total,grade_F_total]
        #print total
        return total

    def total_sex(self):
    	"""
		Create a Function called total_sex that returns the count for the number of males and females for the entire dataset
		[Male, Female] 
		"""
        M,F = 0,0
        for i in self.data:
            if i[1] == "M":
                M += 1
            else:
                F += 1
        total = [M, F]
        #print total
        return total

if __name__ == '__main__':

    classnumba1().total_avg()
    classnumba1().total_mid_avg()
    classnumba1().total_change()
    classnumba1().total_grade_count()
    classnumba1().total_sex()












