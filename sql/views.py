from django.shortcuts import render;
import sqlite3;

#Content developed by Chris
from django.http import HttpResponse;


def index(request):
    return HttpResponse('\'/rebuild_db\'');

#Rebuild the database table schema. THIS ACTION DELETES ALL RECORDS FROM ALL NON-DJANGO TABLES AND IS NOT REVERSIBLE.
def rebuild_db(request):
    conn = sqlite3.connect('vmc_tap.db');
    return_statement = 'Schema rebuilt!<br>';

    # Store table list
    remove_tables = ['student_barcode'];

    tables = ['visits', 'demographics', 'tags', 'logins', 'cat_hours', 'gpa'];

    # Remove tables
    for t in remove_tables:
        conn.execute('DROP TABLE IF EXISTS ' + t + ';');
    for t in tables:
        conn.execute('DROP TABLE IF EXISTS ' + t + ';');

    # Recreate tables
    #The visits table should contain records of student visits, but no information about the student's personal data. This table should be the 'many' part of a one-to-many relationship with the demographics table. The automatically generated ROWID field serves as the primary key, but it links to the demographics table on the student_id field.
    conn.execute(
        'CREATE TABLE visits(student_name TEXT, student_email TEXT, student_id INTEGER, services TEXT, location TEXT, check_in_date DATE, check_in_time TEXT, check_out_date DATE, check_out_time TEXT, check_in_duration REAL, staff_name TEXT, staff_email TEXT, staff_id TEXT)');

    #The demographics table contains information about the students who visit the center. There should be one record per student, and it should be updated whenever new information comes in. While this table has an automatically generated ROWID field that works as a primary key, the student_id field also can work as a primary key.
    conn.execute(
        'CREATE TABLE demographics(student_name TEXT, student_email TEXT, student_id INTEGER,  classification TEXT, major TEXT, benefit_chapter INTEGER, is_stem INTEGER, currently_live TEXT, employment TEXT, work_hours TEXT, dependents TEXT, marital_status TEXT, gender TEXT, parent_education TEXT, break_in_attendance TEXT, pell_grant TEXT, needs_based TEXT, merit_based TEXT, federal_work_study TEXT, military_grants TEXT, millennium_scholarship TEXT, nevada_prepaid TEXT, contact_method TEXT)');

    #The gpa table contains information about a student's GPA for a given semester. This table should be the 'many' part of a one-to-many relationship with the demographics table. Each student can have multiple semesters worth of GPA data. The ROWID field serves as the primary key.
    conn.execute('CREATE TABLE gpa(student_id INTEGER, date DATE, end_term_cumulative_gpa REAL, end_term_term_gpa REAL, end_term_attempted_credits REAL, end_term_earned_credits REAL, end_term_credit_completion REAL)');


    #The cat_hours table is used as a reference point for reports that provide information about the frequency of visits based upon the hour of the day.
    #It is a static table that does not accept new records. There are 24 records; one for each hour of the day.
    conn.execute('CREATE TABLE cat_hours(hour_display TEXT, ordering INTEGER)');
    conn.execute("INSERT INTO cat_hours VALUES ('12 AM', 0)");
    for i in range(1,12):
        conn.execute("INSERT INTO cat_hours VALUES ('" + str(i) +" AM', " + str(i) + ")");
    conn.execute("INSERT INTO cat_hours VALUES ('12 PM', 12)");
    for i in range(1,12):
        conn.execute("INSERT INTO cat_hours VALUES ('" + str(i) +" PM', " + str(i+12) + ")");

    #The tags table was designed as the 'many' part of a one-to-many relationship with the demographics table. Since the tags field in the Excel sheet for student visits provided a
    #comma-delimited list of tags for the student, it preserved database normal form to break it up into a one-to-many relationship. However, this table is defunct; the tags data
    #just does not get imported into this table.
    conn.execute('CREATE TABLE tags(student_id INTEGER, tag TEXT, date TEXT)');
    conn.commit();

    return_statement = return_statement + '\n\n\n';

    #Print out table schema
    for t in tables:
        return_statement = return_statement + t + ':<br>';
        return_statement = return_statement + 'cid, name, type, notnull, defaultval, pk<br>';
        for a in conn.execute('PRAGMA table_info(\'' + t + '\');'):
            return_statement = return_statement + (', '.join([str(b) for b in a])) + '<br>';

        return_statement = return_statement + '<br>';
    conn.close();
    return HttpResponse(return_statement);
