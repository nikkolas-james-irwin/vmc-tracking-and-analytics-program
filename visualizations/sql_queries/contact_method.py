# Returns the SQL query for total visits by contact method based on user-provided location, from date, and to date
def get_query(from_time, to_time, substr):
    return "SELECT demographics.contact_method, count(demographics.contact_method) " \
           "FROM visits LEFT JOIN demographics ON visits.student_id = demographics.student_id " \
           "WHERE (location = \'" + substr + "\') and check_in_date >= \'" + from_time + "\' " \
            "AND check_in_date <= \'" + to_time + "\' and demographics.contact_method " \
                                                  "is not null GROUP BY demographics.contact_method;"