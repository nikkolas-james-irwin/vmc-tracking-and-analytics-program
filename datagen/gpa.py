import sqlite3 #sqlite library
import csv #csv writer library 
import random #random generation library


#header for all gpa datafiles
#JH
gpa_header = 'Report Name: Count Students in End Term,,,,,,\nReport Description: Count Students in End Term,,,,,,\n,,,,,,\nApplied filters:,"(SELECT Count Students in End Term BY Student By Term Key, ALL OTHER) > 0",,,,,\n,Boolean FIlter Name IN (In),,,,,\n,"Campaign Owner IN (Borthwick-Wong, Emilly)",,,,,\n,Term Name IN (2021 Spring),,,,,\n,,,,,,\n'

#Get a list of all students in the database to generate gpa data for them
#JH
def get_students():
    conn = sqlite3.connect('vmc_tap.db')
    cur  = conn.cursor()
    cur.execute('select distinct student_id, student_name from visits')
    students = cur.fetchall()
    return students

#Generates a gpa data point for each student in the databse
#Returns the csvfile with the passed in filename
#JH
def gen_gpa_data(filename):
    data = []
    students = get_students()
    for student in students:
        data.append(gen_gpa(student))
    csvfile = open(filename, 'a+')
    csvfile.write(gpa_header)
    csvwriter = csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(['ID','Name','End Term Cumulitive GPA', 'End Term GPA', 'End Term Attempted Credits', 'End Term Earned Credits', 'End Term % Credit Completion'])
    for point in data:
        csvwriter.writerow(point)
    csvfile.close()

#generates random gpa data for a student
#JH
def gen_gpa(student):
    student_id = student[0]
    student_name = student[1]
    cumm_gpa = (random.randint(0,20)+20)/10
    term_gpa = (random.randint(0,20)+20)/10
    term_credits = random.randint(10,18)
    earned_credits = random.randint(0,term_credits)
    comp_percent = (earned_credits/term_credits)*100
    return [student_id,student_name,cumm_gpa,term_gpa,term_credits,earned_credits,comp_percent]


