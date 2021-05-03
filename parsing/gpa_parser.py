import csv

#class for GPA data
#each row in the csvfile should be parsed into a different GPAData class object
#JH
class GPAData:
    student_id = ''
    student_name = ''
    cum_gpa = ''
    term_gpa = ''
    term_credits = ''
    earned_credits = ''
    comp_percent = ''
    term = ''

    def __init__(self, row, term):
        self.student_id = row[0]
        self.student_name = row[1]
        self.cum_gpa = row[2]
        self.term_gpa = row[3]
        self.term_credits = row[4]
        self.earned_credits = row[5]
        self.comp_percent = row[6]
        self.term = term

    #Inserts the data from the GPA class into the gpa table as a single record
    #Chris
    def get_insert_statement(self):
        insert_val_names = ['student_id','date','end_term_cumulative_gpa','end_term_term_gpa', 'end_term_attempted_credits', 'end_term_earned_credits', 'end_term_credit_completion'];
        insert_val_list = [self.student_id, self.term, self.cum_gpa, self.term_gpa, self.term_credits, self.earned_credits, self.comp_percent];
        insert_val_list = ['\"' + str(a) + '\"' for a in insert_val_list];

        return 'INSERT INTO gpa (' + ', '.join(insert_val_names) + ') VALUES (' + ', '.join(insert_val_list) + ');'


#removes the header info from the raw data
#Params raw_data: The raw data from the csvfile
#Returns the raw data without the header info
#JH
def remove_header(raw_data):
    term = ''
    for i in range(0,len(raw_data)):
        temp_str = raw_data[i][1]
        if temp_str != '':
            temp_str = temp_str.split(' ')
            if temp_str[0] == 'Term':
                temp_str = raw_data[i][1].split('(')
                term = temp_str[1].split(')')[0]
        if raw_data[i][0] == 'ID':
            return raw_data[i:],term

#iterates over the rows in a csvfile and returns a list of GPAData class objects
#Params csvfile: the csvfile to be parsed
#Returns formatted: A list of GPAData class objects
#JH
def parse_gpa(csvfile):
    reader = csv.reader(csvfile, delimiter=',')
    data = []
    for row in reader:
        data.append(row)
    if data[0][0] != 'Report Name: Count Students in End Term':
        return ["ERROR","Invalid header in GPA File"]
    data,term = remove_header(data)
    columns = data[0]
    data = data [1:]
    formatted = []
    for point in data:
        formatted.append(GPAData(point,term))
    return formatted


